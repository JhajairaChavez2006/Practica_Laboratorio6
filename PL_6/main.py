#Llamar funciones
from utils import mostrar_bienvenida, calcular_operaciones, validar_correo

while True:

    print("\n========== MENÚ ==========")
    print("1. Mostrar bienvenida")
    print("2. Calcular suma y promedio")
    print("3. Validar correo")
    print("4. Salir")
    print("==========================")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":

        mostrar_bienvenida()

    elif opcion == "2":

        try:
            #Solicitar numeros
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))

            suma, promedio = calcular_operaciones(num1, num2)