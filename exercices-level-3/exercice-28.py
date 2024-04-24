'''Escribir un programa que pregunte por consola el precio de un
 producto en euros con dos decimales y muestre por pantalla el número de euros y 
el número de céntimos del precio introducido.'''
print("""
  PAPA
  CEBOLLA
  ZANAHORIA
  CARNE    
""")
precio = float(input("Ingrese el precio de un producto: "))
print(precio)
print(f"{int(precio)} euros")
resultado = float(precio) - int(precio)
print(f"{int(resultado*100)+1} centimos")
