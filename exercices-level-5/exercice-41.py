'''Escribir un programa que pregunte al usuario su edad y muestre por 
pantalla todos los años que ha cumplido (desde 1 hasta su edad).'''

edad = int(input("Enter your age: "))
i = 1
while i <= edad:
    print(f"años que has cumplido: {i}")
    i += 1
