# app/console/producto_console.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.db.models.base import EntityBase
from app.db.models import producto  # importa modelos para que SQLAlchemy los registre
from app.schemas.producto import ProductoCreate, ProductoUpdate
from app.repositories.producto_repository import ProductoRepository

DATABASE_URL = "sqlite:///./inventario.db"
engine = create_engine(DATABASE_URL, echo=False)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def main():
    EntityBase.metadata.create_all(bind=engine)
    db = SessionLocal()
    repo = ProductoRepository(db)

    while True:
        print("\n1. Crear producto")
        print("2. Listar productos")
        print("3. Actualizar producto")
        print("4. Eliminar producto")
        print("0. Salir")
        opcion = input("Ingrese opción: ")

        if opcion == "1":
            nombre = input("Nombre del producto: ")            
            sku = input("SKU: ")
            descripcion = input("Descripción: ")
            producto_in = ProductoCreate(nombre=nombre, sku=sku, descripcion=descripcion)
            producto = repo.create_producto(producto_in)
            print("Producto creado:", producto)

        elif opcion == "2":
            productos = repo.get_all_productos()
            for p in productos:
                print(f"[{p.id}] {p.nombre} - {p.descripcion}")
        
        elif opcion == "3":
            id_ = int(input("ID del producto a actualizar: "))
            nombre = input("Nuevo nombre (dejar vacío para no cambiar): ").strip() or None
            sku = input("Nuevo SKU (dejar vacío para no cambiar): ").strip() or None
            descripcion = input("Nueva descripción (dejar vacío para no cambiar): ").strip() or None
            producto_upd = ProductoUpdate(nombre=nombre, sku=sku, descripcion=descripcion)
            updated = repo.update_producto(id_, producto_upd)
            if updated:
                print("Producto actualizado:", updated)
            else:
                print("No se encontró producto con ese ID.")
        elif opcion == "4":
            id_ = int(input("ID del producto a eliminar: "))
            deleted = repo.delete_producto(id_)
            if deleted:
                print("Producto eliminado.")
            else:
                print("No se encontró producto con ese ID.")

        elif opcion == "0":
            break

        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()
