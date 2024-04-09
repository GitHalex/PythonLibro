'''Definir una función superposicion() que tome dos listas y devuelva True si tienen al menos 1
miembro en común o devuelva False de lo contrario. Escribir la función usando el bucle for
anidado. '''


def superposicion(lista1, lista2):
    en_comun = False
    for i in lista1:
        for j in lista2:
            if i == j:
                en_comun = True
                break

    return en_comun


print(superposicion([1, 2, 3], [6, 7, 3]))
