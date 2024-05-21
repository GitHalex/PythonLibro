'''Escribir un programa que almacene en una lista los siguientes 
precios, 50, 75, 46, 22, 80, 65, 8, y muestre por pantalla el menor y el mayor de los precios.'''
listaPrecios = [50, 75, 46, 22, 80, 65, 8]
print(listaPrecios)
menor = listaPrecios[0]
mayor = listaPrecios[0]
for num in listaPrecios:
    if num < menor:
        menor = num
    if num > mayor:
        mayor = num

print(f"{menor} es el numero menor")
print(f"{mayor} es el numero mayor")
