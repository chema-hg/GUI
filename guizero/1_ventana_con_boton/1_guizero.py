from guizero import *

def claro():
    boton.bg = "#ececec"
    boton.when_mouse_leaves = oscuro

def oscuro():
    boton.bg = "#d9d9d9"


raiz=App(title="Aplicación", bg='beige', width=300, height=200)

boton = PushButton(raiz, text='Salir', align='bottom', padx=25, pady=2, command=quit)
boton.bg="#d9d9d9"

boton.when_mouse_enters = claro

raiz.display()