# mappers/usuario_mapper.py
from app.domain.models.usuario import Usuario
from app.db.models.usuario import UsuarioORM
from mappers.rol_mapper import rol_orm_to_domain, rol_domain_to_orm

def usuario_orm_to_domain(orm: UsuarioORM) -> Usuario:
    roles = [rol_orm_to_domain(r) for r in orm.roles] if orm.roles else []
    return Usuario(
        id=orm.id,
        username=orm.username,
        email=orm.email,
        hashed_password=orm.hashed_password,
        is_active=orm.is_active,
        roles=roles
    )

def usuario_domain_to_orm(domain: Usuario) -> UsuarioORM:
    orm = UsuarioORM(
        username=domain.username,
        email=domain.email,
        hashed_password=domain.hashed_password,
        is_active=domain.is_active,
    )
    if domain.id is not None:
        orm.id = domain.id
    if domain.roles:
        orm.roles = [rol_domain_to_orm(r) for r in domain.roles]
    else:
        orm.roles = []
    return orm
