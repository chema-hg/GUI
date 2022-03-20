# importamos la ventana principal, una caja y un botón
from guizero import App, Box, PushButton

def set():
    print("Hola Mundo")
    
# Creamos la aplicación principal
app = App(width=200, height=150)

# Creamos una caja alineada a la izquierda que ocupe toda la ventana y con borde
# para que podamos verlo.
box = Box(app)
# Colocamos el botón con una serie de propiedades iniciales
boton = PushButton(box, text="Botón1", command=set)
# Propiedades adicionales de los botones
boton.bg="light blue"
boton.text_color="red"
# incluso podemos usar directamente un método de tkinter en guizero
# <nombre>.tk.config()
boton.tk.config(bd=2, relief = "groove",font = "Verdana 14 underline")
boton.tk.pack(pady=5)

app.display()