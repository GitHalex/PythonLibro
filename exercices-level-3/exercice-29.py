'''Escribir un programa que pregunte al usuario la fecha de su 
nacimiento en formato dd/mm/aaaa y muestra por pantalla, el día, el mes y el año.
 Adaptar el programa anterior para que también funcione cuando
 el día o el mes se introduzcan con un solo carácter.'''


nacimiento = input("Ingrese su flecha de nacimiento en formato dd/mm/aaaa: ")
print(f"Dia: {nacimiento[0:2]}")
print(f"Mes: {nacimiento[3:5]}")
print(f"Año: {nacimiento[6:]}")
