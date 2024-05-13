'''Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo 
como el de más abajo, de altura el número introducido.

*
**
***
****
***** '''
cantidad = int(input("Ingrese un numero: "))
indice = 1
caracter = ""
while indice <= cantidad:
    caracter += "#"
    print(caracter)
    indice += 1
