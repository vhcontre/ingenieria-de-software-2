# app/repositories/deposito_repository.py
from sqlalchemy.orm import Session
from app.db.models.deposito import DepositoORM
from app.domain.models.deposito import Deposito
from app.schemas.deposito import DepositoCreate, DepositoUpdate
from app.domain.mappers.deposito_mapper import deposito_orm_to_domain


class DepositoRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_deposito(self, deposito_in: DepositoCreate) -> Deposito:
        nuevo_orm = DepositoORM(nombre=deposito_in.nombre, ubicacion=deposito_in.ubicacion)
        self.db.add(nuevo_orm)
        self.db.commit()
        self.db.refresh(nuevo_orm)
        return deposito_orm_to_domain(nuevo_orm)

    def get_deposito(self, deposito_id: int) -> Deposito | None:
        orm = self.db.query(DepositoORM).filter(DepositoORM.id == deposito_id).first()
        return deposito_orm_to_domain(orm) if orm else None

    def get_all_depositos(self) -> list[Deposito]:
        orms = self.db.query(DepositoORM).all()
        return [deposito_orm_to_domain(orm) for orm in orms]

    def update_deposito(self, deposito_id: int, deposito_in: DepositoUpdate) -> Deposito | None:
        orm = self.db.query(DepositoORM).filter(DepositoORM.id == deposito_id).first()
        if orm is None:
            return None
        if deposito_in.nombre is not None:
            orm.nombre = deposito_in.nombre
        if deposito_in.ubicacion is not None:
            orm.ubicacion = deposito_in.ubicacion
        self.db.commit()
        self.db.refresh(orm)
        return deposito_orm_to_domain(orm)

    def delete_deposito(self, deposito_id: int) -> bool:
        orm = self.db.query(DepositoORM).filter(DepositoORM.id == deposito_id).first()
        if orm is None:
            return False
        self.db.delete(orm)
        self.db.commit()
        return True
