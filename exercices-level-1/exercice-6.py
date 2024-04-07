'''Definir una función inversa() que calcule la inversión de una cadena. Por ejemplo la cadena
"estoy probando" debería devolver la cadena "odnaborp yotse"'''


def inversa(cadena):
    revertido = ""
    i = len(cadena)
    while i >= 0:
        revertido += cadena[i]
        i += 1
    return revertido


print(inversa("hola"))
