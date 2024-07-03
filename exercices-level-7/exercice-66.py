'''Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y
 lo guarde en un diccionario. Después debe mostrar por pantalla el mensaje <nombre> tiene <edad> años,
  vive en <dirección> y su número de teléfono es <teléfono>.'''
datos = {}
nombre = input("Ingrese un nombre: ")
edad = int(input("Ingrese su edad: "))
direccion = input("Ingrese su direccion: ")
telefeno = int(input("Ingrese su celular: "))
datos[nombre] = (edad, direccion, telefeno)
print(datos)
for name in datos:
    print(
        f"{name} tiene: {datos[name][0]} años vive en: {datos[name][1]} y su numero de telefono es: {datos[name][2]}")
