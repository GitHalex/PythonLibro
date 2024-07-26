'''Escribir un programa que cree un diccionario vacío y lo vaya llenado con 
información sobre una persona (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.)
 que se le pida al usuario. Cada vez que se añada un nuevo dato debe imprimirse el contenido del diccionario.'''


def solicitar_datos():
    """Solicita información del usuario para llenar un diccionario."""
    persona = {}
    continuar = True

    while continuar:
        clave = input(
            "Ingrese el tipo de información (por ejemplo, nombre, edad, sexo, teléfono, correo electrónico): ")
        valor = input(f"Ingrese el valor para {clave}: ")
        persona[clave] = valor

        print("Contenido actual del diccionario:")
        for k, v in persona.items():
            print(f"{k}: {v}")

        continuar = input(
            "¿Desea ingresar otro dato? (s/n): ").strip().lower() == 's'

    return persona


if __name__ == "__main__":
    diccionario_persona = solicitar_datos()
    print("\nContenido final del diccionario:")
    for k, v in diccionario_persona.items():
        print(f"{k}: {v}")
