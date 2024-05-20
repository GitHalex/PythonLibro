'''Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo.'''


def esPalindromo(cadena: str):
    reversa = cadena[::-1]
    return reversa


cadena = input("Ingrese una palabra: ")

if cadena == esPalindromo(cadena):
    print(f"{cadena} = {esPalindromo(cadena)} es 'PALINDROMO'")
else:
    print(f"{cadena} = {esPalindromo(cadena)} no es 'PALINDROMO'")
