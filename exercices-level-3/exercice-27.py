'''Escribir un programa que pregunte el correo electrónico del usuario en la consola y 
muestre por pantalla otro correo electrónico con el mismo nombre 
(la parte delante de la arroba @) pero con dominio ceu.es.'''
email = input("Ingrese su correo electronico: ")
posicion = email.find("@")
print(posicion)
print(email[0:posicion])
nuevoDominio = email[0:posicion+1] + "ceu.es"
print(nuevoDominio)
