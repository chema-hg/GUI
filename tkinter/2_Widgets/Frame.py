from tkinter import *
import tkinter.ttk as ttk
# Creamos la aplicacion principal y su tamaño
raiz = Tk()
raiz.geometry("200x150")

# Creamos una caja alineada a la izquierda que ocupe toda la ventana y con borde
# para que podamos verlo.
frame=Frame(raiz)
frame.config(bg="lightblue")
frame.pack(side="left", fill="x", expand=1)

# Colocamos un boton dentro del Frame
button=Button(frame,text="botón")
button.pack()
# Colocamos otro boton dentro del mismo Frame
button1= Button(frame, text="Otro botón")
button1.pack()

raiz.mainloop()
