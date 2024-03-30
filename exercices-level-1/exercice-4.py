'''Escribir una función que tome un carácter y devuelva True si es una vocal, de lo contrario
devuelve False.'''


def caracter(char):
    es_vocal = False
    if len(char) == 1:
        char_convertido = char.lower()
        print(char_convertido)
        if char_convertido == "a" or char_convertido == "e" or char_convertido == "i" or char_convertido == "o" or char_convertido == "u":
            es_vocal = True

    else:
        print(f"{char} introduciste mas de un caracter")
        es_vocal = False

    return f"el {char} es vocal?? {es_vocal}"


print(caracter("a"))
print(caracter("aaa"))
