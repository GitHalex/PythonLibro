'''Escribir un programa que almacene la cadena de caracteres contraseña 
en una variable, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña 
introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas. '''

password = "hola1"
passWord_usuario = input("Cual es la contraseña: ")

if password == passWord_usuario.lower():
    print("la contraseña es correcta")
else:
    print("La contraseña no es la correcta")
