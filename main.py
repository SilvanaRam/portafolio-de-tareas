print("Convertidor Decimal-Binario")

while True:
    print("\nSelecciona una opción:")
    print("1. Decimal a Binario")
    print("2. Binario a Decimal")
    print("3. Salir")

    opcion = input("Ingresa el número de la opción: ")

    if opcion == '1':
        decimal = int(input("Ingresa un número decimal: "))
        binario = bin(decimal)[2:]  # Utilizamos la función 'bin' de Python para la conversión
        print(f"El número binario equivalente es: {binario}")
        break  # Salimos del bucle después de la conversión
    elif opcion == '2':
        binario = input("Ingresa un número binario: ")
        decimal = int(binario, 2)  # Utilizamos 'int' para la conversión de binario a decimal
        print(f"El número decimal equivalente es: {decimal}")
        break  # Salimos del bucle 
    elif opcion == '3':
        print("¡Hasta luego!")
        break  # Salimos del
        print("Opción no válida. Por favor, elige 1, 2 o 3.")
