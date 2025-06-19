#file: backend/app/routers/depositos.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.deposito import DepositoCreate, DepositoRead
from app.db.session import get_db
from app.repositories.deposito_repository import DepositoRepository
from app.dependencies.security import get_current_user  # Usa el nombre estándar

router = APIRouter()

@router.post(
    "/",
    response_model=DepositoRead,
    status_code=201,
    summary="Crear un nuevo depósito",
    description="Crea un depósito en el sistema. Requiere autenticación.",
    responses={
        201: {"description": "Depósito creado exitosamente"},
        400: {"description": "Datos inválidos"},
        401: {"description": "No autenticado"},
    },
    tags=["Depósitos"],
)
def crear_deposito_endpoint(
    deposito: DepositoCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),  # Protege el endpoint
):
    """
    Crea un nuevo depósito.

    - **nombre**: Nombre del depósito.
    - **ubicacion**: Ubicación del depósito (opcional).
    """
    repo = DepositoRepository(db)
    return repo.create_deposito(deposito)

@router.get(
    "/{deposito_id}",
    response_model=DepositoRead,
    summary="Obtener un depósito por ID",
    description="Devuelve la información de un depósito específico dado su ID. Requiere autenticación.",
    responses={
        200: {"description": "Depósito encontrado"},
        404: {"description": "Depósito no encontrado"},
        401: {"description": "No autenticado"},
    },
    tags=["Depósitos"],
)
def obtener_deposito(
    deposito_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),  # Protege el endpoint
):
    """
    Recupera un depósito por su ID.

    - **deposito_id**: ID del depósito a buscar.
    """
    repo = DepositoRepository(db)
    deposito = repo.get_deposito_by_id(deposito_id)
    if not deposito:
        raise HTTPException(status_code=404, detail="Depósito no encontrado")
    return deposito