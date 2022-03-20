from guizero import App, MenuBar
def file_function():
    pass #codigo a rellenar

def edit_function():
    pass #codigo a rellenar
    
def exit_function():
    app.destroy()

app = App(width=200, height=150)
menubar = MenuBar(app,
                  toplevel=["Save", "Load", "Exit"],
                  options=[
                      [ ["Guardar", file_function], ["Guardar como..", file_function] ],
                      [ ["Cargar", edit_function], ["Cargar archivo", edit_function] ],
                      [ ["Salir", exit_function]],
                  ])
app.display()
