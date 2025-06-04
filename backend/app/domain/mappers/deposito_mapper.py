from app.domain.models.deposito import Deposito
from app.db.models.deposito import DepositoORM

def deposito_orm_to_domain(orm: DepositoORM) -> Deposito:
    return Deposito(
        id=orm.id,
        nombre=orm.nombre,
        ubicacion=orm.ubicacion
    )

def deposito_domain_to_orm(domain: Deposito) -> DepositoORM:
    return DepositoORM(
        id=domain.id,
        nombre=domain.nombre,
        ubicacion=domain.ubicacion
    )
