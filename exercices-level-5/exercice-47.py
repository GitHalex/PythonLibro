'''Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo 
como el de más abajo.

1
3 1
5 3 1
7 5 3 1
9 7 5 3 1'''

numero = int(input("Tamaño de triangulo: "))

for i in range(1, numero + 1):
    if i % 2 != 0:  # Solo procesar números impares
        for j in range(i, 0, -2):
            print(j, end=" ")
        print()  # Nueva línea después de cada fila


i = 1
imprimir = ""
aux = 1
while i <= numero:
    imprimir = str(i) + " " + imprimir
    print(imprimir)
    i += 1
