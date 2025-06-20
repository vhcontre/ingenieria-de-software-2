import uuid
import pytest
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.db.models.base import EntityBase
from app.db.models.producto import ProductoORM
from app.db.models.usuario import UsuarioORM
from app.db.models.deposito import DepositoORM
from app.repositories.movimiento_repository import MovimientoRepository
from app.domain.models.movimiento import Movimiento, TipoMovimiento as DomainTipoMovimiento

# Configuración de la base de datos en memoria
@pytest.fixture(scope="module")
def engine():
    engine = create_engine("sqlite:///:memory:", echo=False)
    EntityBase.metadata.create_all(bind=engine)
    yield engine
    EntityBase.metadata.drop_all(bind=engine)

@pytest.fixture
def db_session(engine):
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session
    session.rollback()  # Hacemos rollback en lugar de close para mantener la transacción
    session.close()

@pytest.fixture
def repo(db_session):
    return MovimientoRepository(db_session)

@pytest.fixture
def fecha_actual():
    return datetime.utcnow()

@pytest.fixture
def usuario_prueba(db_session):
    usuario = UsuarioORM(username="test_user", email="test@example.com", hashed_password="hashed_pw")
    db_session.add(usuario)
    db_session.commit()
    return usuario

@pytest.fixture
def deposito_prueba(db_session):
    deposito = DepositoORM(nombre="Depósito Central", ubicacion="Calle Olivos 7123")
    db_session.add(deposito)
    db_session.commit()
    return deposito

@pytest.fixture
def producto_con_stock(db_session):
    sku = f"SKU-{uuid.uuid4().hex[:8]}"
    producto = ProductoORM(nombre="Producto Test", sku=sku, stock=10)
    db_session.add(producto)
    db_session.commit()
    return producto

def test_ingreso_exitoso(repo, db_session, producto_con_stock, usuario_prueba, deposito_prueba, fecha_actual):
    # Configuración del movimiento
    movimiento = Movimiento(
        id=None,
        producto_id=producto_con_stock.id,
        deposito_origen_id=None,
        deposito_destino_id=deposito_prueba.id,
        usuario_id=usuario_prueba.id,
        cantidad=5,
        fecha=fecha_actual,
        tipo=DomainTipoMovimiento.ingreso,
        timestamp=fecha_actual
    )

    # Ejecución
    movimiento_creado = repo.create_movimiento(movimiento)
    db_session.refresh(producto_con_stock)

    # Aserciones
    assert movimiento_creado.id is not None
    assert movimiento_creado.cantidad == 5
    assert producto_con_stock.stock == 15  # Verifica que el stock se actualizó correctamente
    assert movimiento_creado.tipo == DomainTipoMovimiento.ingreso

def test_egreso_exitoso(repo, db_session, usuario_prueba, deposito_prueba, fecha_actual):
    # Configuración
    sku = f"SKU-{uuid.uuid4().hex[:8]}"
    producto = ProductoORM(nombre="Producto Egreso", sku=sku, stock=20)
    db_session.add(producto)
    db_session.commit()

    movimiento = Movimiento(
        id=None,
        producto_id=producto.id,
        deposito_origen_id=deposito_prueba.id,
        deposito_destino_id=None,
        usuario_id=usuario_prueba.id,
        cantidad=8,
        fecha=fecha_actual,
        tipo=DomainTipoMovimiento.egreso,
        timestamp=fecha_actual
    )

    # Ejecución
    movimiento_creado = repo.create_movimiento(movimiento)
    db_session.refresh(producto)

    # Aserciones
    assert movimiento_creado.cantidad == 8
    assert producto.stock == 12
    assert movimiento_creado.tipo == DomainTipoMovimiento.egreso

def test_egreso_stock_insuficiente(repo, db_session, usuario_prueba, deposito_prueba, fecha_actual):
    # Configuración
    sku = f"SKU-{uuid.uuid4().hex[:8]}"
    producto = ProductoORM(nombre="Producto Insuficiente", sku=sku, stock=3)
    db_session.add(producto)
    db_session.commit()

    movimiento = Movimiento(
        id=None,
        producto_id=producto.id,
        deposito_origen_id=deposito_prueba.id,
        deposito_destino_id=None,
        usuario_id=usuario_prueba.id,
        cantidad=5,
        fecha=fecha_actual,
        tipo=DomainTipoMovimiento.egreso,
        timestamp=fecha_actual
    )

    # Ejecución y verificación de excepción
    with pytest.raises(ValueError) as excinfo:
        repo.create_movimiento(movimiento)
    
    # Aserciones
    assert "Stock insuficiente" in str(excinfo.value)
    db_session.refresh(producto)
    assert producto.stock == 3  # El stock no debe haber cambiado

def test_listado_movimientos_por_producto(repo, db_session, producto_con_stock, usuario_prueba, deposito_prueba, fecha_actual):
    # Configuración de movimientos
    mov_ingreso = Movimiento(
        id=None,
        producto_id=producto_con_stock.id,
        deposito_origen_id=None,
        deposito_destino_id=deposito_prueba.id,
        usuario_id=usuario_prueba.id,
        cantidad=3,
        fecha=fecha_actual,
        tipo=DomainTipoMovimiento.ingreso,
        timestamp=fecha_actual
    )
    
    mov_egreso = Movimiento(
        id=None,
        producto_id=producto_con_stock.id,
        deposito_origen_id=deposito_prueba.id,
        deposito_destino_id=None,
        usuario_id=usuario_prueba.id,
        cantidad=2,
        fecha=fecha_actual,
        tipo=DomainTipoMovimiento.egreso,
        timestamp=fecha_actual
    )

    # Ejecución
    repo.create_movimiento(mov_ingreso)
    repo.create_movimiento(mov_egreso)
    
    # Obtención de resultados
    movimientos = repo.get_by_producto(producto_con_stock.id)
    
    # Aserciones
    assert movimientos is not None
    assert len(movimientos) == 2
    assert all(m.producto_id == producto_con_stock.id for m in movimientos)
    
    # Verificación adicional de tipos de movimiento
    tipos = {m.tipo for m in movimientos}
    assert DomainTipoMovimiento.ingreso in tipos
    assert DomainTipoMovimiento.egreso in tipos