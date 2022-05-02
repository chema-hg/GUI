from guizero import App, Text

# En guizero cuando le pasas un parametro a la funcion llamada por un evento
# le da a la funcion una serie de datos

def keyPressEvent(evento):
    text.value = "You pressed {}".format(evento.key)

app = App(title="Key Press Example", width=320, height=200)
app.when_key_pressed = keyPressEvent

text = Text(app)
text.value = "Press a key"