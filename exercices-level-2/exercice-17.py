'''Escribir un programa que pregunte al usuario una cantidad a invertir, 
el interés anual y el número de años, y muestre por pantalla 
el capital obtenido en la inversión.'''
cantidad_invertir = int(input("Ingrese la cantidad a invertir: "))
interes_anual = int(input("Interes anual: "))
number_years = int(input("Numero de años: "))

capital_obtenido = cantidad_invertir*(1+5/100)**number_years
print(f"Capital obtenido en la inversion: {capital_obtenido}")
