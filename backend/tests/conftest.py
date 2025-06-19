# tests/conftest.py
import sys
import os
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from app.db.models.base import EntityBase
from app.db.session import get_db
from fastapi.testclient import TestClient
from app.main import app

# ✅ SUGERENCIA: asegurar que el PYTHONPATH esté bien en ambientes externos (como GitHub Actions)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))

# Usar SQLite en memoria para test
TEST_DATABASE_URL = "sqlite:///:memory:"

engine_test = create_engine(
    TEST_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine_test)

# Crear y eliminar las tablas una sola vez por sesión de tests
@pytest.fixture(scope="session", autouse=True)
def setup_test_db():
    EntityBase.metadata.create_all(bind=engine_test)
    yield
    EntityBase.metadata.drop_all(bind=engine_test)

# Fixture para generar una sesión de DB nueva en cada test
@pytest.fixture()
def db_session():
    session = TestingSessionLocal()
    try:
        yield session
    finally:
        session.close()

# Cliente de FastAPI con base de datos sobreescrita para usar tests aislados
@pytest.fixture()
def client():
    def override_get_db():
        db = TestingSessionLocal()
        try:
            yield db
        finally:
            db.close()

    app.dependency_overrides[get_db] = override_get_db

    with TestClient(app) as c:
        yield c

# Limpiar todas las tablas después de cada test (muy útil para mantener aislamiento)
@pytest.fixture(autouse=True)
def limpiar_tablas(db_session):
    yield
    for tabla in reversed(EntityBase.metadata.sorted_tables):
        db_session.execute(tabla.delete())
    db_session.commit()
