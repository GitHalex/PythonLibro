'''Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, 
Física, Química, Historia y Lengua) en una lista y la muestre por pantalla. '''
asignaturas = []
while True:
    materias = input("Ingrese una materia: ")
    if materias == "salir":
        break
    else:
        asignaturas.append(materias)

print(asignaturas)
