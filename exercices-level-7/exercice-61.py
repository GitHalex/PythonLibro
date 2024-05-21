'''Escribir un programa que pida al usuario una palabra y muestre por pantalla
 el número de veces que contiene cada vocal.'''
palabra = input("Ingrese una palabra: ")
cantA = 0
cantE = 0
cantI = 0
cantO = 0
cantU = 0
for char in palabra:
    minusculaChar = char.lower()
    if minusculaChar == "a":
        cantA += 1
    if minusculaChar == "e":
        cantE += 1
    if minusculaChar == "i":
        cantI += 1
    if minusculaChar == "o":
        cantO += 1
    if minusculaChar == "u":
        cantU += 1

if cantA > 0:
    print(f"catidad de a: {cantA}")
if cantE > 0:
    print(f"catidad de e: {cantE}")
if cantI > 0:
    print(f"catidad de i: {cantI}")
if cantO > 0:
    print(f"catidad de o: {cantO}")
if cantU > 0:
    print(f"catidad de u: {cantU}")
