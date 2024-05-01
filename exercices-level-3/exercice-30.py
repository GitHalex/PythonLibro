'''Escribir un programa que pregunte por consola por los productos de una cesta de la compra,
 separados por comas, y muestre por pantalla
 cada uno de los productos en una línea distinta.'''
productos = input("""
Productos de compra separados por comas:
""")

# Dividir la entrada por comas
lista_productos = productos.split(',')

# Mostrar cada producto en una línea distinta
for producto in lista_productos:
    # Utiliza strip() para eliminar los espacios en blanco alrededor de cada producto
    print(producto.strip())
