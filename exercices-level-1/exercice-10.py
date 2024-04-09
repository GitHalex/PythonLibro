'''Definir un histograma procedimiento() que tome una lista de números enteros e imprima un
histograma en la pantalla. Ejemplo: procedimiento([4, 9, 7]) debería imprimir lo siguiente:
****
*********
******* '''


def procedimiento(lista):
    cadena = "*"
    histograma = ""
    for i in lista:
        histograma += f"{cadena*i}\n"

    return histograma


print(procedimiento([4, 9, 7]))
