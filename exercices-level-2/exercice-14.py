'''Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. 
Después debe mostrar por pantalla la paga que le corresponde.'''
horas_trabajadas = int(input("Cantidad de horas que ah trabajado: "))
costo_hora = int(input("Costo por hora de trabajo: "))
costo_por_trabajo = horas_trabajadas*costo_hora
print(f"ganaste por las horas de trabajo: {costo_por_trabajo} pelucholares")
