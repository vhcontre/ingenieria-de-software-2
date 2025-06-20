import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime

from app.db.models.base import EntityBase
from app.db.models.producto import ProductoORM
from app.repositories.movimiento_repository import MovimientoRepository
from app.domain.models.movimiento import Movimiento, TipoMovimiento as DomainTipoMovimiento

# Configurar engine y sesión en memoria
engine = create_engine("sqlite:///:memory:", echo=False)
TestingSessionLocal = sessionmaker(bind=engine)

@pytest.fixture(scope="module")
def db_session():
    # Crear tablas en memoria
    EntityBase.metadata.create_all(bind=engine)
    session = TestingSessionLocal()
    yield session
    session.close()
    EntityBase.metadata.drop_all(bind=engine)

@pytest.fixture
def repo(db_session):
    return MovimientoRepository(db_session)

@pytest.fixture
def fecha_actual():
    return datetime.utcnow()

def test_ingreso_exitoso(repo, db_session, fecha_actual):
    # Insertar un producto con stock 10
    producto = ProductoORM(nombre="Producto Test", sku="SKU123", stock=10)
    db_session.add(producto)
    db_session.commit()
    db_session.refresh(producto)

    movimiento = Movimiento(
        id=None,
        producto_id=producto.id,
        deposito_origen_id=None,
        deposito_destino_id=1,
        usuario_id=1,
        cantidad=5,
        fecha=fecha_actual,
        tipo=DomainTipoMovimiento.ingreso,
        timestamp=fecha_actual
    )

    movimiento_creado = repo.create_movimiento(movimiento)
    db_session.refresh(producto)

    assert movimiento_creado.cantidad == 5
    assert producto.stock == 15  # 10 + 5

def test_egreso_exitoso(repo, db_session, fecha_actual):
    producto = ProductoORM(nombre="Producto Egreso", sku="SKU124", stock=20)
    db_session.add(producto)
    db_session.commit()
    db_session.refresh(producto)

    movimiento = Movimiento(
        id=None,
        producto_id=producto.id,
        deposito_origen_id=1,
        deposito_destino_id=None,
        usuario_id=1,
        cantidad=8,
        fecha=fecha_actual,
        tipo=DomainTipoMovimiento.egreso,
        timestamp=fecha_actual
    )

    movimiento_creado = repo.create_movimiento(movimiento)
    db_session.refresh(producto)

    assert movimiento_creado.cantidad == 8
    assert producto.stock == 12  # 20 - 8

def test_egreso_stock_insuficiente(repo, db_session, fecha_actual):
    producto = ProductoORM(nombre="Producto Insuficiente", sku="SKU125", stock=3)
    db_session.add(producto)
    db_session.commit()
    db_session.refresh(producto)

    movimiento = Movimiento(
        id=None,
        producto_id=producto.id,
        deposito_origen_id=1,
        deposito_destino_id=None,
        usuario_id=1,
        cantidad=5,
        fecha=fecha_actual,
        tipo=DomainTipoMovimiento.egreso,
        timestamp=fecha_actual
    )

    with pytest.raises(ValueError) as excinfo:
        repo.create_movimiento(movimiento)
    assert "Stock insuficiente" in str(excinfo.value)

def test_listado_movimientos_por_producto(repo, db_session, fecha_actual):
    # Insertar producto
    producto = ProductoORM(nombre="Producto Listado", sku="SKU126", stock=10)
    db_session.add(producto)
    db_session.commit()
    db_session.refresh(producto)

    # Crear movimientos
    mov1 = Movimiento(
        id=None,
        producto_id=producto.id,
        deposito_origen_id=None,
        deposito_destino_id=1,
        usuario_id=1,
        cantidad=3,
        fecha=fecha_actual,
        tipo=DomainTipoMovimiento.ingreso,
        timestamp=fecha_actual
    )
    mov2 = Movimiento(
        id=None,
        producto_id=producto.id,
        deposito_origen_id=1,
        deposito_destino_id=None,
        usuario_id=1,
        cantidad=2,
        fecha=fecha_actual,
        tipo=DomainTipoMovimiento.egreso,
        timestamp=fecha_actual
    )
    repo.create_movimiento(mov1)
    repo.create_movimiento(mov2)

    try:
        movimientos = repo.get_by_producto(producto.id)
    except Exception:
        db_session.rollback()  # limpia estado fallido
        raise
    
    assert len(movimientos) == 2
    assert all(m.producto_id == producto.id for m in movimientos)
