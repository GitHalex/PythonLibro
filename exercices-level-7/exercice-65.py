'''Escribir un programa que guarde en una variable el
 diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, pregunte al
 usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario.'''


def consulta(divisaDict: dict) -> None:
    clave = input("Ingrese una divisa: Euro-Dollar-Yen :")
    for moneda in divisaDict:
        if clave == moneda:
            print(f"{moneda} => {divisaDict[moneda]}")
            break
        else:
            print(f"No existe divisa: {clave} en  {divisaDict}")
            break


divisa = {'Euro': '€', 'Dollar': '$', 'Yen': '¥'}
consulta(divisa)
