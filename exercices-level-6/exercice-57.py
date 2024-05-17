'''Escribir un programa que almacene en una lista los números del 1 al 10 y los muestre 
por pantalla en orden inverso separados por comas.'''
i = 1
listaNumeros = []
while i <= 10:
    listaNumeros.append(i)
    i += 1


def listaInversa(listaNumeros: list) -> list:
    tam = len(listaNumeros) - 1
    while tam >= 0:
        print(listaNumeros[tam])
        tam -= 1


listaInversa(listaNumeros)
