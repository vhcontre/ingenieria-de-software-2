import uuid
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.db.models.base import EntityBase
from app.db.models.producto import ProductoORM
from app.repositories.producto_repository import ProductoRepository

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
    session.rollback()
    session.close()

@pytest.fixture
def repo(db_session):
    return ProductoRepository(db_session)

@pytest.fixture
def producto_ejemplo(db_session):
    sku = f"SKU-{uuid.uuid4().hex[:8]}"
    producto = ProductoORM(nombre="Producto Test", sku=sku, stock=10, stock_minimo=2)
    db_session.add(producto)
    db_session.commit()
    return producto

def test_crear_producto(repo, db_session):
    sku = f"SKU-{uuid.uuid4().hex[:8]}"
    producto = ProductoORM(nombre="Nuevo Producto", sku=sku, stock=5, stock_minimo=1)
    db_session.add(producto)
    db_session.commit()
    assert producto.id is not None
    assert producto.nombre == "Nuevo Producto"
    assert producto.stock == 5

def test_get_producto_por_id(repo, producto_ejemplo):
    prod = repo.get_producto_by_id(producto_ejemplo.id)
    assert prod is not None
    assert prod.id == producto_ejemplo.id
    assert prod.nombre == producto_ejemplo.nombre

def test_actualizar_producto(repo, db_session, producto_ejemplo):
    producto_ejemplo.nombre = "Producto Actualizado"
    db_session.commit()
    prod = repo.get_producto_by_id(producto_ejemplo.id)
    assert prod.nombre == "Producto Actualizado"

def test_eliminar_producto(repo, db_session, producto_ejemplo):
    prod_id = producto_ejemplo.id
    db_session.delete(producto_ejemplo)
    db_session.commit()
    prod = repo.get_producto_by_id(prod_id)
    assert prod is None
