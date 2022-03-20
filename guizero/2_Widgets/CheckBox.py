from guizero import App, CheckBox, Box

# Creamos la aplicación principal
app = App(width=200, height=150)

# Creamos una contenedor
box = Box(app)
# Incorporamos las casillas de verificación.
checkbox_1 = CheckBox(box, text="Opción1")
checkbox_1 = CheckBox(box, text="Opción2")

app.display()
