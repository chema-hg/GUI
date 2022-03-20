from guizero import App, Window, PushButton

def open_window():
    window.show(wait=True)

app = App(title="My app", height=200, width=200)
# La ventana esta creada pero la ocultamos para que no se vea
# hasta que se pulse el botón que la vuelva visible.
window = Window(app, title = "2nd ventana", height=150, width=150)
window.hide()

open=PushButton(app, text="Segunda ventana", command=open_window)

app.display()