from fastapi import FastAPI
from app.routers import auth, usuarios, admin, productos, depositos, movimientos  



app = FastAPI()
app.include_router(auth.router)
app.include_router(usuarios.router)
app.include_router(admin.router)
app.include_router(depositos.router, prefix="/depositos")
app.include_router(productos.router, prefix="/productos", tags=["productos"])
app.include_router(movimientos.router, prefix="/movimientos", tags=["movimientos"])
