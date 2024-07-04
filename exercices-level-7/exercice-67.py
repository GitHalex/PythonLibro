'''Escribir un programa que pregunte una fecha en formato dd/mm/aaaa 
y muestre por pantalla la misma fecha en formato dd de <mes> de aaaa donde <mes> es el nombre del mes.'''


def obtener_nombre_mes(mes: int) -> str:
    meses = [
        "enero", "febrero", "marzo", "abril", "mayo", "junio",
        "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"
    ]
    return meses[mes - 1]


def convertir_fecha(fecha: str) -> str:
    partes = fecha.split('/')
    dia = partes[0]
    mes = int(partes[1])
    anio = partes[2]

    nombre_mes = obtener_nombre_mes(mes)
    return f"{dia} de {nombre_mes} de {anio}"


# Solicitar al usuario que ingrese la fecha
fecha_input = input("Ingrese una fecha en formato dd/mm/aaaa: ")
fecha_convertida = convertir_fecha(fecha_input)
print(fecha_convertida)
