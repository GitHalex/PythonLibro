'''Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no. '''
numero = int(input("Ingrese un numero: "))

# Verificar si el número es menor que 2
if numero < 2:
    esPrimo = False
else:
    esPrimo = True
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            esPrimo = False
            break  # Salir del bucle si se encuentra un divisor

if esPrimo:
    print(f"El numero {numero} es primo")
else:
    print(f"El numero {numero} no es primo")
