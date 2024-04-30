'''Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.'''

edad = int(input("Ingrese su edad: "))
if edad >= 18:
    print("Es mayor de edad!!!")
elif edad > 0:
    print("Es menor de edad!!!")
else:
    print("La edad {edad} introducida es 0 o numero negativo")
