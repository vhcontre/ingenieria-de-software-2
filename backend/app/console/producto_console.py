# app/console/producto_console.py

from app.db.session import SessionLocal
from app.schemas.producto import ProductoCreate, ProductoUpdate
from app.repositories.producto_repository import ProductoRepository

def crear_producto(repo):
    nombre = input("Nombre del producto: ")            
    sku = input("SKU: ")
    descripcion = input("Descripción: ")
    producto_in = ProductoCreate(nombre=nombre, sku=sku, descripcion=descripcion)
    producto = repo.create_producto(producto_in)
    print("Producto creado:", producto)

def listar_productos(repo):
    productos = repo.get_all_productos()
    for p in productos:
        print(f"[{p.id}] {p.nombre} - {p.sku} - {p.descripcion}")

def actualizar_producto(repo):
    try:
        id_ = int(input("ID del producto a actualizar: "))
    except ValueError:
        print("ID inválido.")
        return
    nombre = input("Nuevo nombre (dejar vacío para no cambiar): ").strip() or None
    sku = input("Nuevo SKU (dejar vacío para no cambiar): ").strip() or None
    descripcion = input("Nueva descripción (dejar vacío para no cambiar): ").strip() or None
    producto_upd = ProductoUpdate(nombre=nombre, sku=sku, descripcion=descripcion)
    updated = repo.update_producto(id_, producto_upd)
    if updated:
        print("Producto actualizado:", updated)
    else:
        print("No se encontró producto con ese ID.")

def eliminar_producto(repo):
    try:
        id_ = int(input("ID del producto a eliminar: "))
    except ValueError:
        print("ID inválido.")
        return
    deleted = repo.delete_producto(id_)
    if deleted:
        print("Producto eliminado.")
    else:
        print("No se encontró producto con ese ID.")

def main():    
    repo = ProductoRepository(SessionLocal())

    menu = {
        "1": lambda: crear_producto(repo),
        "2": lambda: listar_productos(repo),
        "3": lambda: actualizar_producto(repo),
        "4": lambda: eliminar_producto(repo),
    }

    while True:
        print("\n1. Crear producto")
        print("2. Listar productos")
        print("3. Actualizar producto")
        print("4. Eliminar producto")
        print("0. Salir")
        opcion = input("Ingrese opción: ")

        if opcion == "0":
            break
        elif opcion in menu:
            menu[opcion]()
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()
