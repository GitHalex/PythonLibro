'''Escribir un programa que almacene las asignaturas de un curso 
(por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, 
pregunte al usuario la nota que ha sacado en cada asignatura y elimine de la lista
 las asignaturas aprobadas. Al final el programa debe mostrar por pantalla las asignaturas
  que el usuario tiene que repetir.'''


'''Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, 
Física, Química, Historia y Lengua) en una lista y la muestre por pantalla. '''


def asignaturasLista():
    asignaturas = []
    while True:
        materias = input("Ingrese una materia: ")
        if materias == "salir":
            break
        else:
            asignaturas.append(materias)
    return asignaturas


# Lista de asignaturas
asignaturas = asignaturasLista()

# Diccionario para almacenar las notas de cada asignatura
notas = {}

# Preguntar al usuario la nota de cada asignatura y almacenarla en el diccionario
for asignatura in asignaturas:
    nota = input(f"Nota de {asignatura}: ")
    notas[asignatura] = nota
    if int(nota) > 50:
        del notas[asignatura]

# Mostrar las notas de cada asignatura
print("--------NOTAS DE MATERIAS REPORBADAS----------")
for asignatura, nota in notas.items():
    print(f"En {asignatura} has sacado: {nota}")
