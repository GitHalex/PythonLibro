'''Escribir un programa que pida al usuario un número entero positivo
 y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas. '''

numero = int(input("Ingrese un numero entero positivo: "))
inicio = 1
impares = []  # Lista para almacenar los números impares

while inicio <= numero:
    if inicio % 2 != 0:
        impares.append(inicio)  # Agrega el número impar a la lista
    inicio += 1

# Imprime los números impares separados por comas
print(*impares, sep=",")
