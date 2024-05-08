'''La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes.
 Los ingredientes para cada tipo de pizza aparecen a continuación.

Ingredientes vegetarianos: Pimiento y tofu.
Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.

Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, 
y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija.
 Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas.
  Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.'''


tipo_pizza = input(
    "Que tipo de pizza quieres 'vegetariana' o 'no vegetariana'")
pizza_elegidad = ""
if tipo_pizza == 'vegetariana':
    print("""
############################################################
#                    PIZZERIA BELLA NAPOLI                 #
#                                                          #
#  -Ingredientes vegetarianos: pimiento y tufo             #
#                                                          #
#                                                          #
############################################################
""")
    ingredientes = input("elija un ingrediente: ")
    con_mozarela_tomate = input("con mozarela y tomate? 'si' o 'no' :")
    if ingredientes == "pimiento":
        if con_mozarela_tomate == 'si':
            pizza_elegidad = f"{ingredientes} con mozarela y tomate: {con_mozarela_tomate}"
        if con_mozarela_tomate == 'no':
            pizza_elegidad = f"{ingredientes} sin mozarela y tomate: {con_mozarela_tomate}"

    if ingredientes == "tufo":
        if con_mozarela_tomate == 'si':
            pizza_elegidad = f"{ingredientes} con mozarela y tomate: {con_mozarela_tomate}"
        if con_mozarela_tomate == 'no':
            pizza_elegidad = f"{ingredientes} sin mozarela y tomate: {con_mozarela_tomate}"


if tipo_pizza == "no vegetariana":
    print("""
############################################################
#                    PIZZERIA BELLA NAPOLI                 #
#                                                          #
#                                                          #
#  -Ingredientes no vegetarianos: peperoni, jamon y salmon #
#                                                          #
############################################################
""")
    ingredientes = input("elija un ingrediente: ")
    con_mozarela_tomate = input("con mozarela y tomate? 'si' o 'no' :")
    if ingredientes == "peperoni":
        if con_mozarela_tomate == 'si':
            pizza_elegidad = f"{ingredientes} con mozarela y tomate: {con_mozarela_tomate}"
        if con_mozarela_tomate == 'no':
            pizza_elegidad = f"{ingredientes} sin mozarela y tomate: {con_mozarela_tomate}"

    if ingredientes == "jamon":
        if con_mozarela_tomate == 'si':
            pizza_elegidad = f"{ingredientes} con mozarela y tomate: {con_mozarela_tomate}"
        if con_mozarela_tomate == 'no':
            pizza_elegidad = f"{ingredientes} sin mozarela y tomate: {con_mozarela_tomate}"

    if ingredientes == "jamon":
        if con_mozarela_tomate == 'si':
            pizza_elegidad = f"{ingredientes} con mozarela y tomate: {con_mozarela_tomate}"
        if con_mozarela_tomate == 'no':
            pizza_elegidad = f"{ingredientes} sin mozarela y tomate: {con_mozarela_tomate}"


print(f"tipo de pizza {tipo_pizza}: con {pizza_elegidad}")
