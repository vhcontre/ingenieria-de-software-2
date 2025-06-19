# app/repositories/producto_repository.py

from sqlalchemy.orm import Session
from app.db.models.producto import ProductoORM
from app.domain.models.producto import Producto
from app.schemas.producto import ProductoCreate, ProductoUpdate
from app.domain.mappers.producto_mapper import producto_domain_to_orm, producto_orm_to_domain
from app.utils.validations import check_unicidad_producto

class ProductoRepository:
    def __init__(self, db: Session):
        self.db = db
            
    # producto_repository.py
    def create_producto(self, producto_in: ProductoCreate) -> Producto:
        check_unicidad_producto(self.db, producto_in.nombre, producto_in.sku)        
        
        domain_model = Producto(id=None, nombre=producto_in.nombre, sku=producto_in.sku, descripcion=producto_in.descripcion,
                                stock=producto_in.stock or 0,
                                stock_minimo=producto_in.stock_minimo or 0 )
        
        orm_obj = producto_domain_to_orm(domain_model)
        self.db.add(orm_obj)
        self.db.commit()
        self.db.refresh(orm_obj)
        return producto_orm_to_domain(orm_obj)

    def get_all_productos(self) -> list[Producto]:
        productos = self.db.query(ProductoORM).all()
        return [producto_orm_to_domain(p) for p in productos]

    def get_producto_by_id(self, id_: int) -> Producto | None:
        producto = self.db.query(ProductoORM).filter_by(id=id_).first()
        return producto_orm_to_domain(producto) if producto else None

    def update_producto(self, id_: int, producto_upd: ProductoUpdate) -> Producto | None:
        producto = self.db.query(ProductoORM).filter_by(id=id_).first()
        if not producto:
            return None

        if producto_upd.nombre and producto_upd.nombre != producto.nombre:
            check_unicidad_producto(self.db, producto_upd.nombre, None)
            producto.nombre = producto_upd.nombre
        if producto_upd.sku and producto_upd.sku != producto.sku:
            check_unicidad_producto(self.db, None, producto_upd.sku)
            producto.sku = producto_upd.sku
        if producto_upd.descripcion is not None:
            producto.descripcion = producto_upd.descripcion
        if producto_upd.stock is not None:
            producto.stock = producto_upd.stock

        self.db.commit()
        self.db.refresh(producto)
        return producto_orm_to_domain(producto)

    def delete_producto(self, id_: int) -> bool:
        producto = self.db.query(ProductoORM).filter_by(id=id_).first()
        if not producto:
            return False
        self.db.delete(producto)
        self.db.commit()
        return True

    def seed_productos(self):
        if self.db.query(ProductoORM).count() > 0:
            print("La base de datos ya contiene productos. Seed cancelado.")
            return

        productos_demo = [
            ProductoCreate(nombre="Mouse Inalámbrico", sku="SKU001", descripcion="Mouse Logitech con conexión USB y 1600 DPI"),
            ProductoCreate(nombre="Teclado Mecánico", sku="SKU002", descripcion="Teclado Redragon retroiluminado RGB"),
            ProductoCreate(nombre="Monitor 24\"", sku="SKU003", descripcion="Monitor IPS 24 pulgadas Full HD"),
            ProductoCreate(nombre="Notebook Dell", sku="SKU004", descripcion="Laptop Intel Core i5, 8GB RAM, 256GB SSD"),
            ProductoCreate(nombre="Silla Ergonómica", sku="SKU005", descripcion="Silla de oficina con soporte lumbar y altura regulable"),
            ProductoCreate(nombre="Disco SSD 512GB", sku="SKU006", descripcion="Unidad de estado sólido SATA 3 de 512GB"),
            ProductoCreate(nombre="Auriculares Bluetooth", sku="SKU007", descripcion="Auriculares inalámbricos con micrófono y cancelación de ruido"),
            ProductoCreate(nombre="Webcam Full HD", sku="SKU008", descripcion="Cámara web 1080p con micrófono incorporado"),
            ProductoCreate(nombre="Base Enfriadora", sku="SKU009", descripcion="Soporte con ventiladores para notebooks de hasta 17 pulgadas"),
            ProductoCreate(nombre="Router Wi-Fi 6", sku="SKU010", descripcion="Router inalámbrico doble banda con tecnología Wi-Fi 6"),
        ]

        for p in productos_demo:
            self.create_producto(p)

        print("Productos de prueba insertados correctamente.")
