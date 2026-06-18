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

            print(f"La suma es: {suma}")
            print(f"El promedio es: {promedio}")

        except ValueError:
            print("Error: Debe ingresar números válidos.")

    elif opcion == "3":

        correo = input("Ingrese un correo electrónico: ")

        if validar_correo(correo):
            print("Correo válido")
        else:
            print("Correo inválido")

    elif opcion == "4":

        print("Gracias por usar el programa.")
        break

    else:

        print("Opción no válida. Intente nuevamente.")