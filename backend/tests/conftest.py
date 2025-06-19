# tests/conftest.py
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from app.db.models.base import EntityBase
from app.db.session import get_db
from fastapi.testclient import TestClient
from app.main import app


TEST_DATABASE_URL = "sqlite:///:memory:"

engine_test = create_engine(
    TEST_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine_test)

# Setup inicial de base de datos de prueba
@pytest.fixture(scope="session", autouse=True)
def setup_test_db():
    EntityBase.metadata.create_all(bind=engine_test)
    yield
    EntityBase.metadata.drop_all(bind=engine_test)

# Fixture de sesión para los tests
@pytest.fixture()
def db_session():
    session = TestingSessionLocal()
    try:
        yield session
    finally:
        session.close()

# Cliente para probar la API
@pytest.fixture()
def client():
    def override_get_db():
        db = TestingSessionLocal()
        try:
            yield db
        finally:
            db.close()

    # Sobreescribimos la dependencia de DB de FastAPI    
    app.dependency_overrides[get_db] = override_get_db

    with TestClient(app) as c:
        yield c

@pytest.fixture(autouse=True)
def limpiar_tablas(db_session):
    yield
    for tabla in reversed(EntityBase.metadata.sorted_tables):
        db_session.execute(tabla.delete())
    db_session.commit()