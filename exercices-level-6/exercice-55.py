'''Escribir un programa que almacene las asignaturas de un curso
 (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, 
 pregunte al usuario la nota que ha sacado en cada asignatura, y después las muestre por pantalla 
 con el mensaje En <asignatura> has sacado <nota> donde <asignatura> es cada una des las asignaturas
  de la lista y <nota> cada una de las correspondientes notas introducidas por el usuario.'''


# Lista de asignaturas
asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]

# Diccionario para almacenar las notas de cada asignatura
notas = {}

# Preguntar al usuario la nota de cada asignatura y almacenarla en el diccionario
for asignatura in asignaturas:
    nota = input(f"Nota de {asignatura}: ")
    notas[asignatura] = nota

# Mostrar las notas de cada asignatura
for asignatura, nota in notas.items():
    print(f"En {asignatura} has sacado: {nota}")
