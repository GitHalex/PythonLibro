'''Escribir un programa que pregunte el nombre el un producto, 
su precio y un número de unidades y muestre por pantalla una cadena con el nombre del 
producto seguido de su precio unitario con 6 dígitos enteros y 2 decimales, el número de unidades
 con tres dígitos y el coste total con 8 dígitos enteros y 2 decimales.'''
nameProduct = input("PRODUCTO: ")
# utilizar float en lugar de int para permitir deciamales
price = int(input("PRECIO: "))
cantidad = int(input("CANTIDAD: "))
# calcular el costo total
total_cost = price

print(
    f"Nombre del product: {nameProduct}\nPrecio{price:8.2f}\nNumero de unidades: {cantidad:03d}\nCosto total:{total_cost:19.2f}")
