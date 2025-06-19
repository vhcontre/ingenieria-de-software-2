#file: backend/app/domain/mappers/movimiento_mapper.py
from app.domain.models.movimiento import Movimiento, TipoMovimiento as DomainTipoMovimiento
from app.db.models.movimiento import MovimientoORM

def movimiento_orm_to_domain(orm: MovimientoORM) -> Movimiento:
    return Movimiento(
        id=orm.id,
        producto_id=orm.producto_id,
        deposito_origen_id=orm.deposito_origen_id,
        deposito_destino_id=orm.deposito_destino_id,
        usuario_id=orm.usuario_id,
        cantidad=orm.cantidad,
        fecha=orm.fecha,
        tipo=DomainTipoMovimiento(orm.tipo.value),
        timestamp=orm.fecha
    )

def movimiento_domain_to_orm(domain: Movimiento) -> MovimientoORM:
    orm = MovimientoORM(
        producto_id=domain.producto_id,
        deposito_origen_id=domain.deposito_origen_id,
        deposito_destino_id=domain.deposito_destino_id,
        usuario_id=domain.usuario_id,
        cantidad=domain.cantidad,
        fecha=domain.fecha,
        tipo=domain.tipo.value 
    )
    if hasattr(domain, "id") and domain.id is not None:
        orm.id = domain.id
    return orm
