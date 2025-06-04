# app/repositories/producto_repository.py

from sqlalchemy.orm import Session
from app.db.models.producto import ProductoORM
from app.domain.models.producto import Producto
from app.domain.mappers.producto_mapper import producto_domain_to_orm, producto_orm_to_domain
from app.schemas.producto import ProductoCreate, ProductoUpdate


class ProductoRepository:

    def __init__(self, db: Session):
        self.db = db

    def create_producto(self, producto_in: ProductoCreate) -> Producto:
        nuevo_orm = ProductoORM(nombre=producto_in.nombre,sku= producto_in.sku , descripcion=producto_in.descripcion)
        self.db.add(nuevo_orm)
        self.db.commit()
        self.db.refresh(nuevo_orm)
        return producto_orm_to_domain(nuevo_orm)
    
    def update_producto(self, producto_id: int, producto_in: ProductoUpdate) -> Producto | None:
        orm = self.db.query(ProductoORM).filter(ProductoORM.id == producto_id).first()
        if orm is None:
            return None
        if producto_in.nombre is not None:
            orm.nombre = producto_in.nombre
        if producto_in.sku is not None:
            orm.sku = producto_in.sku
        if producto_in.descripcion is not None:
            orm.descripcion = producto_in.descripcion
        self.db.commit()
        self.db.refresh(orm)
        return producto_orm_to_domain(orm)
    
    def delete_producto(self, producto_id: int) -> bool:
        orm = self.db.query(ProductoORM).filter(ProductoORM.id == producto_id).first()
        if orm is None:
            return False
        self.db.delete(orm)
        self.db.commit()
        return True

    def get_producto(self, producto_id: int) -> Producto | None:
        orm = self.db.query(ProductoORM).filter_by(id=producto_id).first()
        return producto_orm_to_domain(orm) if orm else None

    def get_all_productos(self) -> list[Producto]:
        orm_list = self.db.query(ProductoORM).all()
        return [producto_orm_to_domain(orm) for orm in orm_list]
