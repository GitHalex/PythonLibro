'''Definir una función inversa() que calcule la inversión de una cadena. Por ejemplo la cadena
"estoy probando" debería devolver la cadena "odnaborp yotse"'''


def inversa(cadena):
    invertida = ""
    for letra in cadena:
        invertida = letra + invertida
    return invertida


print(inversa("hola"))
