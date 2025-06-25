from fastapi import APIRouter, Request, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.repositories.producto_repository import ProductoRepository 
from app.web_ui import templates

router = APIRouter()

@router.get("/web/productos")
def ver_productos(request: Request, db: Session = Depends(get_db)):
    repo = ProductoRepository(db)
    productos = repo.get_all_productos()
    return templates.TemplateResponse("productos.html", {"request": request, "productos": productos})
