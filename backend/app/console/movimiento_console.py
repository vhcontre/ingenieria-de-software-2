# -*- coding: utf-8 -*-
from datetime import datetime
from app.repositories.movimiento_repository import MovimientoRepository
from app.db.session import SessionLocal
from app.domain.models.movimiento import Movimiento, TipoMovimiento


def registrar_movimiento(repo: MovimientoRepository):
    try:
        producto_id = int(input("ID del producto: "))
        tipo_str = input("Tipo (ingreso/egreso): ").strip().lower()
        tipo = TipoMovimiento(tipo_str)
        cantidad = int(input("Cantidad: "))
        usuario_id = int(input("ID del usuario: "))
        deposito_origen_id = None
        deposito_destino_id = None

        if tipo == TipoMovimiento.egreso:
            deposito_origen_id = int(input("ID del depósito origen: "))
        elif tipo == TipoMovimiento.ingreso:
            deposito_destino_id = int(input("ID del depósito destino: "))

        movimiento = Movimiento(
            id=None,
            producto_id=producto_id,
            deposito_origen_id=deposito_origen_id,
            deposito_destino_id=deposito_destino_id,
            usuario_id=usuario_id,
            cantidad=cantidad,
            fecha=datetime.now(),
            tipo=tipo,
        )

        repo.create_movimiento(movimiento)
        print("Movimiento registrado exitosamente.")
    except Exception as e:
        print(f"Error: {e}")


def listar_movimientos(repo: MovimientoRepository):
    movimientos = repo.get_all()
    print("\n📋 Todos los movimientos:")
    for m in movimientos:
        print(f"[{m.id}] {m.fecha.strftime('%Y-%m-%d %H:%M:%S')} - {m.tipo.value} - "
              f"Prod {m.producto_id} - Cant: {m.cantidad} - Usuario: {m.usuario_id}")


def ver_movimientos_por_producto(repo: MovimientoRepository):
    try:
        producto_id = int(input("ID del producto: "))
        movimientos = repo.get_by_producto(producto_id)
        if movimientos:
            print(f"\nMovimientos del producto {producto_id}:")
            for m in movimientos:
                print(f"[{m.id}] {m.fecha.strftime('%Y-%m-%d %H:%M:%S')} - {m.tipo.value} - "
                      f"Cantidad: {m.cantidad} - Usuario: {m.usuario_id}")
        else:
            print("No hay movimientos para ese producto.")
    except Exception as e:
        print(f"Error: {e}")


def main():
    db = SessionLocal()
    repo = MovimientoRepository(db)

    menu = {
        "1": lambda: registrar_movimiento(repo),
        "2": lambda: listar_movimientos(repo),
        "3": lambda: ver_movimientos_por_producto(repo),
    }

    while True:
        print("\n=== Gestión de Movimientos ===")
        print("1. Registrar nuevo movimiento")
        print("2. Listar todos los movimientos")
        print("3. Ver movimientos por producto")
        print("0. Volver")
        opcion = input("Ingrese opción: ").strip()

        if opcion == "0":
            break
        accion = menu.get(opcion)
        if accion:
            accion()
        else:
            print("Opción inválida.")


if __name__ == "__main__":
    main()
