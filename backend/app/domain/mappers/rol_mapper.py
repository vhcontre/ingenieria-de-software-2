# mappers/rol_mapper.py
from app.domain.models.rol import Rol
from app.db.models.usuario import RolORM 

def rol_orm_to_domain(orm: RolORM) -> Rol:
    return Rol(
        id=orm.id,
        nombre=orm.nombre,
    )

def rol_domain_to_orm(domain: Rol) -> RolORM:
    orm = RolORM(
        nombre=domain.nombre,
    )
    if domain.id is not None:
        orm.id = domain.id
    return orm
