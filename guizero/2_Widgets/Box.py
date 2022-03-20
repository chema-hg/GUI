# importamos la ventana principal, una caja y un botón
from guizero import App, Box, PushButton
# Creamos la aplicación principal
app = App(width=200,height=150)
# Creamos una caja alineada a la izquierda que ocupe toda la ventana y con borde
# para que podamos verlo.
box = Box(app, align="left", width="fill", border=2)
# Colocamos un botón
button = PushButton(box)
# Colocamos otro que se pone debajo
button1 = PushButton(box, text="another button")

app.display()


