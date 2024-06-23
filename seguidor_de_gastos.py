import pickle
from transaccion import Transaccion

class SeguidorDeGastos:
    """
    Clase que gestiona el seguimiento de las transacciones financieras.
    """
    def __init__(self):
        """
        Inicializa una nueva instancia de SeguidorDeGastos y carga los datos desde el archivo si existe.
        """
        self.transacciones = []
        self.cargar_datos()
    
    def agregar_transaccion(self, transaccion: Transaccion):
        """
        Agrega una nueva transacción a la lista de transacciones.

        :param transaccion: La transacción a agregar.
        """
        self.transacciones.append(transaccion)
        print("Transacción agregada exitosamente.")
    
    def listar_transacciones(self):
        """
        Lista todas las transacciones ordenadas por fecha.
        """
        if not self.transacciones:
            print("No hay transacciones para mostrar.")
            return
        
        transacciones_ordenadas = sorted(self.transacciones, key=lambda x: x.fecha)
        for transaccion in transacciones_ordenadas:
            print(f"{transaccion.fecha.date()} - {transaccion.descripcion}: {'+' if transaccion.tipo == 'ingreso' else '-'}{transaccion.monto}")
    
    def calcular_balance(self):
        """
        Calcula y muestra el balance actual de ingresos, gastos y capacidad de ahorro.
        """
        if not self.transacciones:
            print("No hay transacciones para calcular el balance.")
            return
        
        ingresos = sum(t.monto for t in self.transacciones if t.tipo == 'ingreso')
        gastos = sum(t.monto for t in self.transacciones if t.tipo == 'gasto')
        capacidad_ahorro = ingresos - gastos
        print(f"Ingresos Totales: {ingresos}")
        print(f"Gastos Totales: {gastos}")
        print(f"Capacidad de Ahorro: {capacidad_ahorro}")
    
    def guardar_datos(self):
        """
        Guarda la lista de transacciones en un archivo utilizando pickle.
        """
        with open('datos_financieros.pkl', 'wb') as file:
            pickle.dump(self.transacciones, file)
        print("Datos guardados exitosamente.")
    
    def cargar_datos(self):
        """
        Carga los datos de transacciones desde un archivo utilizando pickle.
        Si el archivo no existe, inicializa la lista de transacciones como vacía.
        """
        try:
            with open('datos_financieros.pkl', 'rb') as file:
                self.transacciones = pickle.load(file)
            print("Datos cargados exitosamente.")
        except FileNotFoundError:
            print("No se encontraron datos previos.")
        except Exception as e:
            print(f"Ocurrió un error al cargar los datos: {e}")
