#file: backend/app/routers/productos.py
from fastapi import APIRouter, Depends, HTTPException
from app.schemas.producto import ProductoCreate, ProductoRead
from app.db.session import get_db
from sqlalchemy.orm import Session
from app.repositories.producto_repository import ProductoRepository
from app.dependencies.security import get_current_user  # Asegúrate de tener esta función

router = APIRouter()

@router.post(
    "/",
    response_model=ProductoRead,
    status_code=201,
    summary="Crear un nuevo producto",
    description="Crea un producto en el sistema. Requiere autenticación.",
    responses={
        201: {"description": "Producto creado exitosamente"},
        400: {"description": "Datos inválidos"},
        401: {"description": "No autenticado"},
    },
    tags=["Productos"],
)
def crear_producto_endpoint(
    producto: ProductoCreate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user),  # Protege el endpoint
):
    """
    Crea un nuevo producto.

    - **nombre**: Nombre del producto.
    - **sku**: Código SKU único.
    - **stock**: Stock inicial.
    - **stock_minimo**: Stock mínimo permitido.
    """
    repo = ProductoRepository(db)
    return repo.create_producto(producto)

@router.get(
    "/{producto_id}",
    response_model=ProductoRead,
    summary="Obtener un producto por ID",
    description="Devuelve la información de un producto específico dado su ID. Requiere autenticación.",
    responses={
        200: {"description": "Producto encontrado"},
        404: {"description": "Producto no encontrado"},
        401: {"description": "No autenticado"},
    },
    tags=["Productos"],
)
def obtener_producto(
    producto_id: int,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user),  # Protege el endpoint
):
    """
    Recupera un producto por su ID.

    - **producto_id**: ID del producto a buscar.
    """
    repo = ProductoRepository(db)
    producto = repo.get_producto_by_id(producto_id)
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return producto