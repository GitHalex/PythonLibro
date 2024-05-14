'''Escribir un programa en el que se pregunte al usuario por una frase y una letra, 
y muestre por pantalla el número de veces que aparece la letra en la frase.'''
frase = input("Ingrese una frase: ")
character = input("Ingrese un character para buscar en la frase: ")
veces = 0
for char in frase:
    if character == char:
        veces += 1

print(f"la Frase: \n{frase}\ntiene {character}\nse repite {veces} veces")
