'''Escribir un programa que pregunte al usuario los números ganadores de 
la lotería primitiva, los almacene en una lista y los muestre por pantalla ordenados de menor a mayor. '''
numerosGanadores = []
while True:
    number = int(input("Numeros Ganadores: "))
    print("Para salir ingrese un numero negativo: ")
    if number < 0:
        break
    else:
        numerosGanadores.append(number)
numerosGanadores.sort()
print(numerosGanadores)
