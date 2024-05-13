'''Escribir un programa que almacene la cadena de caracteres contraseña en una variable, 
pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.'''

password = "alex123"
while True:
    contrasenia = input("Ingrese una contraseña: ")
    if password == contrasenia:
        print("CONTRASEÑA CORRECTA")
        break
    else:
        print("CONTRASEÑA INCORRECTA")
