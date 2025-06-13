from sqlalchemy.orm import Session

from app.db.models.movimiento import MovimientoORM
from app.db.models.producto import ProductoORM

from app.domain.mappers.movimiento_mapper import (
    movimiento_orm_to_domain,
    movimiento_domain_to_orm,
)
from app.domain.models.movimiento import Movimiento, TipoMovimiento as DomainTipoMovimiento


class MovimientoRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_movimiento(self, movimiento: Movimiento) -> Movimiento:
        # Obtener el producto
        producto = self.db.query(ProductoORM).filter(ProductoORM.id == movimiento.producto_id).first()
        if not producto:
            raise ValueError("Producto no encontrado")

        # Aplicar reglas de stock según el tipo de movimiento
        if movimiento.tipo == DomainTipoMovimiento.egreso:
            if producto.stock < movimiento.cantidad:
                raise ValueError(f"Stock insuficiente. Disponible: {producto.stock}, Requerido: {movimiento.cantidad}")
            producto.stock -= movimiento.cantidad

        elif movimiento.tipo == DomainTipoMovimiento.ingreso:
            producto.stock += movimiento.cantidad

        elif movimiento.tipo == DomainTipoMovimiento.traslado:
            if producto.stock < movimiento.cantidad:
                raise ValueError("Stock insuficiente en origen")
            producto.stock -= movimiento.cantidad

        # Convertir a ORM y guardar
        orm_obj = movimiento_domain_to_orm(movimiento)
        self.db.add(orm_obj)
        self.db.commit()
        self.db.refresh(orm_obj)

        return movimiento_orm_to_domain(orm_obj)

    def get_all(self) -> list[Movimiento]:
        movimientos = self.db.query(MovimientoORM).order_by(MovimientoORM.fecha.desc()).all()
        return [movimiento_orm_to_domain(m) for m in movimientos]

    def get_by_producto(self, producto_id: int) -> list[Movimiento]:
        movimientos = (
            self.db.query(MovimientoORM)
            .filter(MovimientoORM.producto_id == producto_id)
            .order_by(MovimientoORM.fecha.desc())
            .all()
        )
        return [movimiento_orm_to_domain(m) for m in movimientos]
