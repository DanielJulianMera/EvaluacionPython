# Aplicación de Seguimiento de Gastos

## Descripción

Esta es una aplicación de terminal interactiva desarrollada en Python para el seguimiento de gastos personales. Los usuarios pueden registrar sus ingresos y gastos, listar las transacciones ordenadas por fecha y generar un balance financiero.

## Estructura del Proyecto

El proyecto está organizado en tres scripts:

1. `transaccion.py`: Define la clase `Transaccion`.
2. `seguidor_de_gastos.py`: Define la clase `SeguidorDeGastos`.
3. `main.py`: Contiene el menú interactivo y la lógica principal del programa.

## Requisitos

- Python 3.6 o superior.

## Instalación

1. Clona este repositorio en tu máquina local:

    ```bash
    git clone https://github.com/tu_usuario/seguimiento-de-gastos.git
    cd seguimiento-de-gastos
    ```

2. Asegúrate de tener instalado Python 3.6 o superior. Puedes verificarlo con el siguiente comando:

    ```bash
    python --version
    ```

## Uso

### Ejecutar la Aplicación

Para ejecutar la aplicación, simplemente ejecuta el script `main.py`

### Menú Interactivo

Una vez que ejecutes la aplicación, verás el siguiente menú en la terminal:

--- Seguimiento de Gastos ---
1. Agregar Transacción
2. Listar Transacciones
3. Calcular Balance
4. Guardar Datos
5. Salir

### Opciones del Menú

```
1. Agregar Transacción: Permite agregar una nueva transacción (ingreso o gasto).
2. Listar Transacciones: Muestra todas las transacciones ordenadas por fecha.
3. Calcular Balance: Calcula y muestra el balance actual de ingresos, gastos y capacidad de ahorro.
4. Guardar Datos: Guarda las transacciones en un archivo datos_financieros.pkl.
5. Salir: Sale de la aplicación.
```

### Ejemplos de Uso

1. Agregar una Transacción

Sigue los pasos indicados en el menú para agregar una transacción. Por ejemplo:

```
Ingrese el monto: 100.0
Ingrese la fecha (YYYY-MM-DD): 2024-06-01
Ingrese la descripción: Salario
Ingrese el tipo (ingreso/gasto): ingreso
```

2. Listar Transacciones

Selecciona la opción 2 en el menú para listar todas las transacciones:

```
2024-06-01 - Salario: +100.0
2024-06-02 - Renta: -500.0
```

3. Calcular Balance

Selecciona la opción 3 en el menú para calcular el balance actual:

```
Ingresos Totales: 100.0
Gastos Totales: 500.0
Capacidad de Ahorro: -400.0
```

4. Guardar Datos
Selecciona la opción 4 en el menú para guardar las transacciones en un archivo:

```
Datos guardados exitosamente.
```
