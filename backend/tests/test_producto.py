



from backend.app.schemas.producto import ProductoRead
from datetime import datetime

def main():
    # Crear un producto de prueba
    producto_test = ProductoRead(
        id=1,
        nombre= "Laptop" ,
        descripcion = "Laptop con 16GB RAM",
        precio = 1499.99,
        stock = 10,
        fecha_creacion = datetime.utcnow(),
        categoria = "Electrónica"
    )

    # Imprimir el producto
    print(producto_test)

    # Probar algunos atributos
    assert producto_test.nombre == "Laptop"
    assert producto_test.precio == 1499.99
    assert producto_test.stock == 10

    print("¡Test Pydantic Producto OK! ✅")

if __name__ == "__main__":
    main()
