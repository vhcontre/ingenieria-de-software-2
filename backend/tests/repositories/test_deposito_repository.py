import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.db.models.base import EntityBase
from app.db.models.deposito import DepositoORM

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
def deposito_ejemplo(db_session):
    deposito = DepositoORM(nombre="Depósito Central", ubicacion="Calle Olivos 7123")
    db_session.add(deposito)
    db_session.commit()
    return deposito

def test_crear_deposito(db_session):
    deposito = DepositoORM(nombre="Depósito Nuevo", ubicacion="Calle Nueva 123")
    db_session.add(deposito)
    db_session.commit()
    assert deposito.id is not None
    assert deposito.nombre == "Depósito Nuevo"

def test_get_deposito_por_id(db_session, deposito_ejemplo):
    deposito = db_session.query(DepositoORM).filter_by(id=deposito_ejemplo.id).first()
    assert deposito is not None
    assert deposito.id == deposito_ejemplo.id
    assert deposito.nombre == deposito_ejemplo.nombre

def test_actualizar_deposito(db_session, deposito_ejemplo):
    deposito_ejemplo.nombre = "Depósito Actualizado"
    db_session.commit()
    deposito = db_session.query(DepositoORM).filter_by(id=deposito_ejemplo.id).first()
    assert deposito.nombre == "Depósito Actualizado"

def test_eliminar_deposito(db_session, deposito_ejemplo):
    dep_id = deposito_ejemplo.id
    db_session.delete(deposito_ejemplo)
    db_session.commit()
    deposito = db_session.query(DepositoORM).filter_by(id=dep_id).first()
    assert deposito is None
