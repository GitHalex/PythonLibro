'''Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere calcular
 de forma automática el precio que debe cobrar a sus clientes por entrar. El programa debe preguntar al
  usuario la edad del cliente y mostrar el precio de la entrada. Si el cliente es menor de 4 años puede 
  entrar gratis, si tiene entre 4 y 18 años debe pagar 5€ y si es mayor de 18 años, 10€. '''


print("""
#####################################
#  PRECIO                           #
#     * MENORES DE 4 AÑOS GRATIS    #
#     * DE 4 Y 18 AÑOS PRECIO 5BS   #
#     * MAYORES DE 18 PRECIO 10BS   #
#####################################
""")
edad_cliente = int(input("Edad: "))


if edad_cliente > 0 and edad_cliente <= 4:
    print(f"tu edad {edad_cliente} años: ingreso gratuito")
elif edad_cliente > 4 and edad_cliente <= 18:
    print(f" tu edad {edad_cliente} años: precio de entrada 5BS")
else:
    print(f" tu edad {edad_cliente} años: precio de entrada  10BS")
