'''Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. 
El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un nombre
 posterior a la N y el grupo B por el resto. Escribir un programa que pregunte al usuario su nombre y sexo,
  y muestre por pantalla el grupo que le corresponde.'''

nombre = input("Nombre: ")
sexo = input("Sexo: ")
grupo = ""
primerCaracter = nombre[0].upper()
charSexo = sexo.upper()

if (primerCaracter <= "M" and charSexo == "MUJER") or (primerCaracter >= "N" and charSexo == "VARON"):
    grupo = "A"

    print(
        f"Tu nombre: {nombre} y tu sexo es: {sexo} perteneces al grupo: {grupo}")

if (primerCaracter >= "N" and charSexo == "MUJER") or (primerCaracter <= "M" and charSexo == "VARON"):
    grupo = "B"
    print(
        f"Tu nombre: {nombre} y tu sexo es: {sexo} perteneces al grupo: {grupo}")
