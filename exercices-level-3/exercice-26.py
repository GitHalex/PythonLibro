'''Escribir un programa que pida al usuario que introduzca una frase en la consola y una vocal,
 y después muestre por pantalla
 la misma frase pero con la vocal introducida en mayúscula'''
frase = input("Please type a frase: ")
vocal = input("Ingrese una vocal a,e,i,o,u: ")
indice = 0
frase_cambiada = ""
char = ""
while indice < len(frase):
    char = frase[indice]
    if "a" == char and char == vocal:
        frase_cambiada += char.upper()
    elif "e" == char and char == vocal:
        frase_cambiada += char.upper()
    elif "i" == char and char == vocal:
        frase_cambiada += char.upper()
    elif "o" == char and char == vocal:
        frase_cambiada += char.upper()
    elif "u" == char and char == vocal:
        frase_cambiada += char.upper()
    else:
        frase_cambiada += char

    indice += 1

print(frase_cambiada)
