'''Escribir una función a la que se le pase una cadena <nombre> y muestre por pantalla el saludo ¡hola <nombre>!.'''

import tkinter as tk


def prueba_tkinter():
    ventana = tk.Tk()
    ventana.title("Prueba de Tkinter")
    tk.Label(ventana, text="¡Tkinter está funcionando en Ubuntu!").pack(pady=20)
    ventana.mainloop()


prueba_tkinter()
