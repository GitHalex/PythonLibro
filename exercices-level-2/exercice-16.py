'''Escribir un programa que pida al usuario dos números enteros y 
muestre por pantalla la <n> entre <m> da un cociente <c> y un resto <r> donde <n> y <m> son 
los números introducidos por el usuario, y <c> y <r> son el cociente y el resto de la división
 entera respectivamente. '''

numerador = int(input("NUMERADOR: "))
denominador = int(input("DENOMINADOR: "))

cociente = numerador/denominador
residuo = numerador % denominador
print(f"Cociente: {cociente} ---- Denominador: {residuo}")
