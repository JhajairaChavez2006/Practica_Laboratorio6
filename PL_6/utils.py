# Funciones reutilizables del programa

import re

def mostrar_bienvenida():
    """
    Muestra un mensaje de bienvenida.
    Retorna:
        None
    """
    print("\n¡Bienvenido al programa de funciones!")

    #Amir Sáenz
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