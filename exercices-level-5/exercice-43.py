'''Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla
 la cuenta atrás desde ese número hasta cero separados por comas.'''

numero = int(input("Ingrese un numero entero positivo: "))
numeros = []
while numero > 0:
    numeros.append(numero)
    numero -= 1

print(*numeros, sep=",")
