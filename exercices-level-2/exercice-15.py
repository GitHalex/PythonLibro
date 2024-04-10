'''Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros),
 calcule el índice de masa corporal y lo almacene en una variable,
  y muestre por pantalla la frase Tu índice de masa corporal es <imc> donde <imc> es el
   índice de masa corporal calculado
 redondeado con dos decimales. '''
peso = int(input("Ingrese su peso un numero entero:"))
estatura = float(input("Ingrese su estatura en metro un numero flotante"))


def imc(peso, estatura):
    IMC = peso / estatura**2
    return round(IMC)


print(f"El IMC es: {imc(peso, estatura)}")
