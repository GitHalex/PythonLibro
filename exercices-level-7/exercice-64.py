'''Escribir un programa que pregunte por una muestra de números, 
separados por comas, los guarde en una lista y muestre por pantalla su media y desviación típica.'''
import math


def calcular_media(lista_numeros: list) -> float:
    return sum(lista_numeros) / len(lista_numeros)


def calcular_desviacion_estandar(lista_numeros: list, media: float) -> float:
    varianza = sum((x - media) ** 2 for x in lista_numeros) / \
        len(lista_numeros)
    return math.sqrt(varianza)


def main():
    muestra = input("Ingrese una muestra de números, separados por comas: ")
    lista_numeros = [float(num) for num in muestra.split(",")]

    media = calcular_media(lista_numeros)
    desviacion_estandar = calcular_desviacion_estandar(lista_numeros, media)

    print(f"Media: {media}")
    print(f"Desviación típica: {desviacion_estandar}")


if __name__ == "__main__":
    main()
