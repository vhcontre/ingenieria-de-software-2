from fastapi import APIRouter, Depends
from app.schemas.deposito import DepositoCreate, DepositoRead
from app.repositories.deposito_repository import DepositoRepository

from app.db.session import get_db

router = APIRouter()

@router.post("/", response_model=DepositoRead, status_code=201)
def crear_deposito_endpoint(deposito: DepositoCreate, db=Depends(get_db)):
    repo = DepositoRepository(db)
    return repo.create_deposito(deposito)

