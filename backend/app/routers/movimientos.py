#file: backend/app/routers/movimientos.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.movimiento import MovimientoCreate, MovimientoRead
from app.db.session import get_db
from app.repositories.movimiento_repository import MovimientoRepository
from app.dependencies.security import get_current_user

router = APIRouter()

@router.post(
    "/",
    response_model=MovimientoRead,
    status_code=201,
    summary="Registrar un nuevo movimiento",
    description="Registra un movimiento de stock (ingreso, egreso o traslado). Requiere autenticación.",
    responses={
        201: {"description": "Movimiento registrado exitosamente"},
        400: {"description": "Datos inválidos"},
        401: {"description": "No autenticado"},
    },
    tags=["Movimientos"],
)
def crear_movimiento(
    movimiento: MovimientoCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    """
    Registra un nuevo movimiento de stock.

    - **tipo**: Tipo de movimiento (ingreso, egreso, traslado).
    - **fecha**: Fecha del movimiento.
    - **cantidad**: Cantidad de productos.
    - **producto_id**: ID del producto.
    - **deposito_origen_id**: ID del depósito de origen (opcional).
    - **deposito_destino_id**: ID del depósito de destino (opcional).
    - **usuario_id**: ID del usuario que realiza el movimiento.
    """
    repo = MovimientoRepository(db)
    return repo.create_movimiento(movimiento)

@router.get(
    "/{movimiento_id}",
    response_model=MovimientoRead,
    summary="Obtener un movimiento por ID",
    description="Devuelve la información de un movimiento específico dado su ID. Requiere autenticación.",
    responses={
        200: {"description": "Movimiento encontrado"},
        404: {"description": "Movimiento no encontrado"},
        401: {"description": "No autenticado"},
    },
    tags=["Movimientos"],
)
def obtener_movimiento(
    movimiento_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    """
    Recupera un movimiento por su ID.

    - **movimiento_id**: ID del movimiento a buscar.
    """
    repo = MovimientoRepository(db)
    movimiento = repo.get_movimiento_by_id(movimiento_id)
    if not movimiento:
        raise HTTPException(status_code=404, detail="Movimiento no encontrado")
    return movimiento