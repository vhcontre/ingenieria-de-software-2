# app/console/deposito_console.py
from app.db.session import SessionLocal
from app.repositories.deposito_repository import DepositoRepository
from app.schemas.deposito import DepositoCreate, DepositoUpdate

def main():
    repo = DepositoRepository(SessionLocal())

    while True:
        print("\nCRUD Depósitos")
        print("1. Crear depósito")
        print("2. Listar depósitos")
        print("3. Actualizar depósito")
        print("4. Eliminar depósito")
        print("0. Salir")

        opcion = input("Ingrese opción: ")

        if opcion == "1":
            nombre = input("Nombre: ").strip()
            ubicacion = input("Ubicación (opcional): ").strip() or None
            deposito_in = DepositoCreate(nombre=nombre, ubicacion=ubicacion)
            deposito = repo.create_deposito(deposito_in)
            print(f"Depósito creado: {deposito}")

        elif opcion == "2":
            depositos = repo.get_all_depositos()
            for d in depositos:
                print(d)

        elif opcion == "3":
            id_ = int(input("ID a actualizar: "))
            nombre = input("Nuevo nombre (dejar vacío para no cambiar): ").strip() or None
            ubicacion = input("Nueva ubicación (dejar vacío para no cambiar): ").strip() or None
            deposito_upd = DepositoUpdate(nombre=nombre, ubicacion=ubicacion)
            updated = repo.update_deposito(id_, deposito_upd)
            if updated:
                print("Depósito actualizado.")
            else:
                print("No se encontró depósito con ese ID.")

        elif opcion == "4":
            id_ = int(input("ID a eliminar: "))
            deleted = repo.delete_deposito(id_)
            if deleted:
                print("Depósito eliminado.")
            else:
                print("No se encontró depósito con ese ID.")

        elif opcion == "0":
            print("Saliendo...")
            break
        else:
            print("Opción inválida")

if __name__ == "__main__":
    main()
