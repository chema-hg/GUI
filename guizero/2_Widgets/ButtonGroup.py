from guizero import App, ButtonGroup, Text, Box

def update_text():
    seleccionada.value = opciones.value

app = App(width=200, height=150)
opciones = ButtonGroup(app, options=
                              ["Opción 1",
                              "Opción 2"],
                            selected="Opción 1", command=update_text)

caja = Box(app, border=2)
seleccionada = Text(caja, "Opción 1")
app.display()
