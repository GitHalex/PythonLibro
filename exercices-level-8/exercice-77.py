'''Escribir una función que calcule el área de un círculo y otra que calcule 
el volumen de un cilindro usando la primera función.
'''


def area(radio: int) -> int:
    return 3.1416 * radio ** 2


resultado = area(5)
print(resultado)
