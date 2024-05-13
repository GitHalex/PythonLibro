'''Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años,
 y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.'''
invertir = int(input("Cantidad a invertir: "))
interes = int(input("Interes anual: "))
num_year = int(input("Numero de años: "))

capital = invertir*(1+interes/100)**num_year
print(capital)

for year in range(1, num_year + 1):
    capital = invertir*(1+interes/100)**year
    print(f"Año {year}: {capital:.2f}")
