'''Definir una función es_palindromo() que reconoce palíndromos (es decir, palabras que tienen el
mismo aspecto escritas invertidas), ejemplo: es_palindromo ("radar") tendría que devolver True.'''


def palindromo(cadena):
    es_palindromo = False
    cadena_invertida = ""
    for letra in cadena:
        cadena_invertida = letra + cadena_invertida

    if cadena_invertida == cadena:
        es_palindromo = True
    else:
        es_palindromo = False

    return es_palindromo


print(palindromo("radar"))
print(palindromo("12321"))
