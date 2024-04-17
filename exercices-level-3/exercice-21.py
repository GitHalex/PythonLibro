'''Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e 
imprima por pantalla en líneas distintas el nombre del usuario tantas veces como 
el número introducido.'''

name_user = input("Ingrese el nombre de usuario: ")
number = int(input("Ingrese un numero: "))
for i in range(0, number):
    print(name_user)
