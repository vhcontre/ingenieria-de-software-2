#file: backend/app/routers/movimientos.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.movimiento import MovimientoCreate, MovimientoRead
from app.db.session import get_db
from app.repositories.movimiento_repository import MovimientoRepository

router = APIRouter()

@router.post("/", response_model=MovimientoRead, status_code=201)
def crear_movimiento(movimiento_in: MovimientoCreate, db: Session = Depends(get_db)):
    return MovimientoRepository(db).create_movimiento(movimiento_in)
