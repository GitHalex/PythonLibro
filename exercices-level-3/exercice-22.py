'''Escribir un programa que pregunte el nombre completo del usuario en la consola 
y después muestre por pantalla el nombre completo del usuario tres veces, una con todas las letras minúsculas, 
otra con todas las letras mayúsculas y otra solo con la primera letra del nombre y de los apellidos en mayúscula.
 El usuario puede introducir su nombre combinando mayúsculas y minúsculas como quiera. '''

fullName = input("Please type your full Name: ")

for i in [1, 2, 3]:
    if i == 1:
        print(fullName.lower())
    if i == 2:
        print(fullName.upper())
    if i == 3:
        print(fullName.title())
