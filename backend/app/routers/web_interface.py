from fastapi import APIRouter, Request, Depends
from sqlalchemy import false
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.repositories.producto_repository import ProductoRepository 
from app.web_ui import templates


from fastapi import Form
from fastapi.responses import HTMLResponse, RedirectResponse
from app.repositories.movimiento_repository import MovimientoRepository
from datetime import datetime
from app.domain.models.movimiento import Movimiento, TipoMovimiento as DomainTipoMovimiento
from app.db.models.producto import ProductoORM


router = APIRouter()

@router.get("/web/productos", response_class=HTMLResponse)
def ver_productos(request: Request, db: Session = Depends(get_db), msg: str = None):
    repo = ProductoRepository(db)
    productos = repo.get_all_productos()
    return templates.TemplateResponse("productos.html", {
        "request": request,
        "productos": productos,
        "msg": msg
    })

@router.get("/web/alerta_stock", response_class=HTMLResponse)
def low_stock_report(request: Request, db: Session = Depends(get_db)):
    repo = ProductoRepository(db)
    low_stock_products = repo.get_low_stock_products()
    return templates.TemplateResponse("alerta_stock.html", {
        "request": request,
        "productos": low_stock_products
    })





@router.get("/web/movimientos", response_class=HTMLResponse)
def ver_movimientos(request: Request, db: Session = Depends(get_db)):
    repo = MovimientoRepository(db)
    movimientos = repo.get_all()  
    return templates.TemplateResponse("movimientos.html", {
        "request": request,
        "movimientos": movimientos
    })

@router.get("/web/movimientos/nuevo")
def mostrar_formulario_movimiento(request: Request):
    return templates.TemplateResponse("movimiento_form.html", {"request": request})

@router.post("/web/movimientos")
def procesar_formulario_movimiento(
    request: Request,
    producto_id: int = Form(...),
    usuario_id: int = Form(...),
    tipo: str = Form(...),
    cantidad: int = Form(...),
    deposito_origen_id: int = Form(None),
    deposito_destino_id: int = Form(None),
    db: Session = Depends(get_db)
):
    try:
        repo = MovimientoRepository(db)
        # Buscar el producto
        producto = db.query(ProductoORM).filter(ProductoORM.id == producto_id).first()
        if not producto:
            raise ValueError("Producto no encontrado")

        # Validar cantidad positiva
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor a cero.")
            return false

        # Validaciones según tipo
        if tipo == "ingreso" and not deposito_destino_id:
            raise ValueError("Debe indicar un depósito destino.")

        elif tipo == "salida":
            if not deposito_origen_id:
                raise ValueError("Debe indicar un depósito origen.")
            if producto.stock < cantidad:
                raise ValueError(f"Stock insuficiente. Disponible: {producto.stock}, requerido: {cantidad}")

        elif tipo == "traslado":
            if not deposito_origen_id or not deposito_destino_id:
                raise ValueError("Debe indicar ambos depósitos.")
            if deposito_origen_id == deposito_destino_id:
                raise ValueError("Los depósitos deben ser distintos.")
            if producto.stock < cantidad:
                raise ValueError(f"Stock insuficiente para traslado. Disponible: {producto.stock}, requerido: {cantidad}")


        movimiento = Movimiento(
            id=None,
            producto_id=producto_id,
            usuario_id=usuario_id,
            cantidad=cantidad,
            tipo=DomainTipoMovimiento(tipo),
            deposito_origen_id=deposito_origen_id,
            deposito_destino_id=deposito_destino_id,
            fecha=datetime.now().date(),
            timestamp=datetime.now()
        )

        repo.create_movimiento(movimiento)
        return RedirectResponse("/web/productos?msg=ok", status_code=303)

    except Exception as e:
        # Si hay error, renderizamos el formulario con:
        # - los valores que el usuario había puesto
        # - y un mensaje de error
        form_data = {
            "producto_id": producto_id,
            "usuario_id": usuario_id,
            "tipo": tipo,
            "cantidad": cantidad,
            "deposito_origen_id": deposito_origen_id,
            "deposito_destino_id": deposito_destino_id,
        }
        return templates.TemplateResponse(
            "movimiento_form.html",
            {
                "request": request,
                "error": str(e),
                "form_data": form_data
            }
        )
