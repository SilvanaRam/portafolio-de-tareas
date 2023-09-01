# Online Python-3 Compiler (Interpreter)

print ("MENU")
print ("Presiona:\n\n(1) Convertir de binario a decimal")
print ("(2) Convertir de decimal a binario")
print ("(3) Multiplicar")
print ("(4) Dividir")
print ("(5) Sumar")
print ("(6) Restar")
print ("(7) Salir")
opcion_de_menu = int(input("Selecciona tu opción: "))
print ("Tu opción es: " + str(opcion_de_menu))

if opcion_de_menu == 1:
    print ("Convertir de binario a decimal")
    binario = input("Digita un numero binario: ")
    decimal = 0
    longitud = len(binario)
    contador = 0
    binario_rev = binario[::-1]
    
    while contador < longitud:
        if binario_rev[contador] == "1":
            decimal += 2 ** contador
        contador += 1
    
    print ("Tu numero a decimal es: " + str(decimal))
    
elif opcion_de_menu == 2:
    print ("Convertir de decimal a binario")
    decimal = int(input("Ingresa un número decimal: "))
    binario = ""
    cociente = decimal
    
    while cociente != 1:
        residuo = cociente % 2
        cociente = cociente // 2
        binario += str(residuo)
    
    binario = binario + "1" 
    binario = binario[::-1] 
    
    print (binario)
    
elif opcion_de_menu == 3:
    print ("Multiplicar")
    numero1 = float(input("Ingresa el primer número: "))
    numero2 = float(input("Ingresa el segundo número: "))
    resultado = numero1 * numero2
    print ("El resultado de la multiplicación es: " + str(resultado))
    
elif opcion_de_menu == 4:
    print ("Dividir")
    numero1 = float(input("Ingresa el dividendo: "))
    numero2 = float(input("Ingresa el divisor: "))
    
    if numero2 == 0:
        print ("Error: No se puede dividir entre cero.")
    else:
        resultado = numero1 / numero2
        print ("El resultado de la división es: " + str(resultado))
        
elif opcion_de_menu == 5:
    print ("Sumar")
    numero1 = float(input("Ingresa el primer número: "))
    numero2 = float(input("Ingresa el segundo número: "))
    resultado = numero1 + numero2
    print ("El resultado de la suma es: " + str(resultado))
    
elif opcion_de_menu == 6:
    print ("Restar")
    numero1 = float(input("Ingresa el primer número: "))
    numero2 = float(input("Ingresa el segundo número: "))
    resultado = numero1 - numero2
    print ("El resultado de la resta es: " + str(resultado))
    
elif opcion_de_menu == 7:
    print ("Salir")
    
else:
    print ("Opción inexistente")

print ("saliendo...")

        
