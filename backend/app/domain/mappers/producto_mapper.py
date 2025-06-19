# mappers/producto_mapper.py
from app.domain.models.producto import Producto
from app.db.models.producto import ProductoORM

def producto_orm_to_domain(orm: ProductoORM) -> Producto:
    return Producto(
        id=orm.id,
        nombre=orm.nombre,
        sku=orm.sku,
        descripcion=orm.descripcion,
        stock=orm.stock,
        stock_minimo=orm.stock_minimo
    )

def producto_domain_to_orm(domain: Producto) -> ProductoORM:
    orm = ProductoORM(
        nombre=domain.nombre,
        sku=domain.sku,
        descripcion=domain.descripcion,
        stock=domain.stock,
        stock_minimo=domain.stock_minimo
        
    )
    if domain.id is not None:
        orm.id = domain.id
    return orm
