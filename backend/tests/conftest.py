import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from app.db.models.base import EntityBase
from app.db.models.rol import RolORM
from app.db.models.usuario import UsuarioORM
from app.security.auth import obtener_password_hash

from app.db.session import get_db
from fastapi.testclient import TestClient
from app.main import app

# Engine global para todos los tests (en memoria)
TEST_DATABASE_URL = "sqlite:///:memory:"
engine = create_engine(
    TEST_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Limpia y crea las tablas antes de cada test
@pytest.fixture(autouse=True, scope="function")
def setup_database():
    EntityBase.metadata.drop_all(bind=engine)
    EntityBase.metadata.create_all(bind=engine)
    yield
    # No es necesario drop_all aquí, ya que se limpia antes de cada test

# Sesión de base de datos para cada test
@pytest.fixture
def db_session():
    session = TestingSessionLocal()
    yield session
    session.close()

# Cliente de FastAPI con base de datos de test
@pytest.fixture
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

# Fixture para crear usuario admin
@pytest.fixture
def crear_usuario_admin(db_session):
    rol_admin = db_session.query(RolORM).filter_by(nombre="admin").first()
    if not rol_admin:
        rol_admin = RolORM(nombre="admin")
        db_session.add(rol_admin)
        db_session.commit()
    admin = db_session.query(UsuarioORM).filter_by(username="admin").first()
    if not admin:
        admin = UsuarioORM(
            username="admin",
            email="admin@example.com",
            hashed_password=obtener_password_hash("admin123"),
            is_active=True,
            roles=[rol_admin]
        )
        db_session.add(admin)
        db_session.commit()
    return admin