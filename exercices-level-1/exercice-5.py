'''Escribir una funcion sum() y una función multip() que sumen y multipliquen respectivamente
todos los números de una lista. Por ejemplo: sum([1,2,3,4]) debería devolver 10 y multip([1,2,3,4])
debería devolver 24.'''


def sum(lista):
    suma = 0
    for i in lista:
        suma += i
    return suma


def multipl(lista):
    multiplicador = 1
    for i in lista:
        multiplicador *= i

    return multiplicador


print(sum([1, 2, 3, 4]))
print(multipl([1, 2, 3, 4]))
