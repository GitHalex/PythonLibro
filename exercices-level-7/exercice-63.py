'''Escribir un programa que almacene los vectores (1,2,3) y (-1,0,2) en dos listas y 
muestre por pantalla su producto escalar.'''
lista1 = [1, 2, 3]
lista2 = [-1, 0, 2]

# Inicializar el producto escalar en 0
producto_escalar = 0

# Calcular el producto escalar
for i in range(len(lista1)):
    producto_escalar += lista1[i] * lista2[i]

# Imprimir el resultado
print(producto_escalar)
