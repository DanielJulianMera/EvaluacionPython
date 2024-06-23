from datetime import datetime
from typing import Union

class Transaccion:
    """
    Clase que representa una transacción financiera, puede ser un ingreso o un gasto.
    """
    def __init__(self, monto: Union[int, float], fecha: str, descripcion: str, tipo: str):
        """
        Inicializa una nueva instancia de Transaccion.

        :param monto: El monto de la transacción.
        :param fecha: La fecha de la transacción en formato 'YYYY-MM-DD'.
        :param descripcion: Una descripción de la transacción.
        :param tipo: El tipo de transacción ('ingreso' o 'gasto').
        """
        self.monto = monto
        self.fecha = datetime.strptime(fecha, "%Y-%m-%d")
        self.descripcion = descripcion
        self.tipo = tipo
