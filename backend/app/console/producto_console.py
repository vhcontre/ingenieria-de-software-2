# app/console/producto_console.py

from app.db.session import SessionLocal
from app.schemas.producto import ProductoCreate, ProductoUpdate
from app.repositories.producto_repository import ProductoRepository

def crear_producto(repo):
    nombre = input("Nombre del producto: ")
    sku = input("SKU: ")
    descripcion = input("Descripción: ")
    stock = input("Stock inicial (dejar vacío para 0): ").strip()
    try:
        producto_in = ProductoCreate(nombre=nombre, sku=sku, descripcion=descripcion, stock=int(stock) if stock else 0)
        producto = repo.create_producto(producto_in)
        print("Producto creado:", producto)
    except ValueError as e:
        print(f"Error: {e}")

def listar_productos(repo):
    productos = repo.get_all_productos()
    if not productos:
        print("No hay productos registrados.")
        return

    print("\nListado de productos:")
    for i, p in enumerate(productos, start=1):
        print(f"{i}. [{p.id}] {p.nombre} - {p.sku} - {p.descripcion} - {p.stock} unidades")

def listar_productos_paginado(repo, por_pagina=5):
    productos = repo.get_all_productos()
    if not productos:
        print("No hay productos registrados.")
        return

    # total = len(productos)
    pagina = 0

    while True:
        inicio = pagina * por_pagina
        fin = inicio + por_pagina
        bloque = productos[inicio:fin]

        if not bloque:
            print("Fin del listado.")
            break

        print(f"\nPágina {pagina + 1}:")
        for i, p in enumerate(bloque, start=inicio + 1):
            print(f"{i}. [{p.id}] {p.nombre} - {p.sku} - {p.descripcion} - {p.stock} unidades")

        opcion = input("\n[Enter] para ver más, [S] para salir: ").strip().lower()
        if opcion == "s":
            break
        pagina += 1

def actualizar_producto(repo):
    try:
        id_ = int(input("ID del producto a actualizar: "))
    except ValueError:
        print("ID inválido.")
        return
    nombre = input("Nuevo nombre (dejar vacío para no cambiar): ").strip() or None
    sku = input("Nuevo SKU (dejar vacío para no cambiar): ").strip() or None
    descripcion = input("Nueva descripción (dejar vacío para no cambiar): ").strip() or None
    stock = input("Nuevo stock (dejar vacío para no cambiar): ").strip() or None
    producto_upd = ProductoUpdate(nombre=nombre, sku=sku, descripcion=descripcion, stock=int(stock) if stock else None)
    try:
        updated = repo.update_producto(id_, producto_upd)
        if updated:
            print("Producto actualizado:", updated)
        else:
            print("No se encontró producto con ese ID.")
    except ValueError as e:
        print(f"Error: {e}")

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

def seed_productos(repo):
    repo.seed_productos()

def main():
    repo = ProductoRepository(SessionLocal())

    menu = {
        "1": lambda: crear_producto(repo),
        "2": lambda: listar_productos(repo),
        "3": lambda: listar_productos_paginado(repo),
        "4": lambda: actualizar_producto(repo),
        "5": lambda: eliminar_producto(repo),
        "6": lambda: seed_productos(repo),  # nueva opción
    }

    while True:
        print("\nGestión de productos")
        print("1. Crear producto")
        print("2. Listar productos (numerado)")
        print("3. Listar productos (paginado)")
        print("4. Actualizar producto")
        print("5. Eliminar producto")
        print("6. Insertar productos de prueba")
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
