'''Definir una función que calcule la longitud de una lista o una cadena dada. (Es cierto que python
tiene la función len() incorporada, pero escribirla por nosotros mismos resulta un muy buen
ejercicio.'''


def longitud(cadena):
    longitud_cadena = len(cadena)
    return longitud_cadena


cadena = input("Please input a String please: ")
print(f"El tamaño de la cadena es: {longitud(cadena)} caracteres")
