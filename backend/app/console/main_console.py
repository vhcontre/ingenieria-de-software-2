# backend/app/console/main_console.py
from app.console.producto_console import main as producto_menu
from app.console.deposito_console import main as deposito_menu
from app.console.movimiento_console import main as movimiento_menu

def main_menu():
    while True:
        print("\n===== MENÚ PRINCIPAL =====")
        print("1. Gestión de Productos")
        print("2. Gestión de Depósitos")
        print("3. Gestión de Movimientos")
        print("0. Salir")

        opcion = input("Ingrese una opción: ").strip()

        if opcion == "1":
            producto_menu()
        elif opcion == "2":
            deposito_menu()
        elif opcion == "3":
            movimiento_menu()
        elif opcion == "0":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main_menu()
