'''Una panadería vende barras de pan a 3.49€ cada una. 
El pan que no es el día tiene un descuento del 60%. Escribir un programa que comience
 leyendo el número de barras vendidas que no son del día. Después el programa debe mostrar 
 el precio habitual de una barra de pan,
 el descuento que se le hace por no ser fresca y el coste final total.'''

panes_vendidas = int(input("Numero de panes vendidas que no son del dia: "))


pan_de_ayer = 3.49*(60/100)
print(f"precio habitual del pan por unidad es: 3.49$")
print(f"precio de los panes con descuento: {pan_de_ayer}")
print(f"precio del costo total: {pan_de_ayer*panes_vendidas}")
