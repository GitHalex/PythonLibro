'''Escribir un programa que pregunte el nombre del usuario en la consola y
 después de que el usuario lo introduzca muestre por 
 pantalla <NOMBRE> tiene <n> letras, donde <NOMBRE> es el nombre de usuario en mayúsculas y <n> es el número 
 de letras que tienen el nombre.'''

userName = input("Ingrese el nombre de usuario: ")
print(f"Name User: {userName.upper()} tiene {len(userName)} letras")
