from fastapi import FastAPI
from app.routers import auth, usuarios, admin  


app = FastAPI()
app.include_router(auth.router)
app.include_router(usuarios.router)
app.include_router(admin.router)
