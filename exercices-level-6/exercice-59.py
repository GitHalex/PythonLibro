'''Escribir un programa que almacene el abecedario en una lista, elimine de la lista 
las letras que ocupen posiciones múltiplos de 3, y muestre por pantalla la lista resultante.'''
# Crear una lista con el abecedario
listaAbecedario = list('abcdefghijklmnopqrstuvwxyz')

# Crear una nueva lista excluyendo las posiciones múltiplos de 3
resultado = [letra for i, letra in enumerate(
    listaAbecedario) if (i + 1) % 3 != 0]

# Mostrar la lista resultante
print(resultado)
