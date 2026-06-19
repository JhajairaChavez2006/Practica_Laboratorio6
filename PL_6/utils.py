# --- Funciones reutilizables del programa ---

import re

# Función que muestra mensaje de bienvenida al usuario
def mostrar_bienvenida():
    """
    Muestra un mensaje de bienvenida.
    Retorna:
        None
    """
    print("\n¡Bienvenido al programa de funciones!")

# Función que realiza operaciones matemáticas básicas para calcular suma y promedio
def calcular_operaciones(numero1, numero2):
    """
    Calcula el promedio de dos números.
    Parámetros:
      numero1 (float): Primer número.
      numero2 (float): Segundo número.
    Retorna:
      float: Promedio de los números.
    """
    suma = numero1 + numero2
    promedio = suma/2
    return suma, promedio

# Función para validar el formato de un correo electrónico
def validar_correo(correo):
    """
    Valida si una cadena tiene formato de correo electrónico.
    Parámetros:
        correo (str): Correo a validar.
    Retorna:
        bool: True si es válido, False si no lo es.
    """
    patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return bool(re.match(patron, correo))
