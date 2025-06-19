# app/routers/productos.py

from fastapi import APIRouter, Depends, HTTPException
from app.schemas.producto import ProductoCreate, ProductoRead
from app.db.session import get_db
from sqlalchemy.orm import Session
from app.repositories.producto_repository import ProductoRepository


router = APIRouter()

@router.post("/", response_model=ProductoRead, status_code=201)
def crear_producto_endpoint(producto: ProductoCreate, db: Session = Depends(get_db)):
    repo = ProductoRepository(db)
    return repo.create_producto(producto)

@router.get("/{producto_id}", response_model=ProductoRead)
def obtener_producto(producto_id: int, db: Session = Depends(get_db)):
    repo = ProductoRepository(db)
    producto = repo.get_producto_by_id(producto_id)
    if not producto:
        raise HTTPException(status_code=404, detail="Not Found")
    return producto