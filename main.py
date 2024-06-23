from transaccion import Transaccion
from seguidor_de_gastos import SeguidorDeGastos
from datetime import datetime

def mostrar_menu():
    """
    Muestra el menú principal de la aplicación.
    """
    print("\n--- Seguimiento de Gastos ---")
    print("1. Agregar Transacción")
    print("2. Listar Transacciones")
    print("3. Calcular Balance")
    print("4. Guardar Datos")
    print("5. Salir")

def main():
    """
    Función principal que maneja la interacción con el usuario.
    """
    seguidor = SeguidorDeGastos()
    
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            try:
                monto = float(input("Ingrese el monto: "))
                fecha = input("Ingrese la fecha (YYYY-MM-DD): ")
                # Verificar formato de fecha
                datetime.strptime(fecha, "%Y-%m-%d")
                descripcion = input("Ingrese la descripción: ")
                tipo = input("Ingrese el tipo (ingreso/gasto): ")
                if tipo not in ['ingreso', 'gasto']:
                    raise ValueError("Tipo inválido. Debe ser 'ingreso' o 'gasto'.")
                transaccion = Transaccion(monto, fecha, descripcion, tipo)
                seguidor.agregar_transaccion(transaccion)
            except ValueError as e:
                print(f"Entrada inválida: {e}")
            except Exception as e:
                print(f"Ocurrió un error: {e}")
        elif opcion == '2':
            seguidor.listar_transacciones()
        elif opcion == '3':
            seguidor.calcular_balance()
        elif opcion == '4':
            seguidor.guardar_datos()
        elif opcion == '5':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
