from guizero import *
from tkinter import *
from tkinter.ttk import Button # Es importante importar el widget que queramos de esta forma.
# Ya que sino nos cogeria el Buttom de tkinter que es mas feo.

class Aplicacion():
    
    def __init__(self):
        # Definimos la raiz.
        raiz= App(title='Aplicación', bg='beige', width=300, height=200)
        # Vamos a insertar un objeto ttk en guizero
        # Para ello creamos un box para meterlo y lo ponemos abajo con align
        box = Box(raiz, align='bottom')
        # En este caso vamos a definir un boton de tkinter.tkk como se haria en tkinter
        # y lo asignamos al box creado antes con box.tk
        bt = Button(box.tk, text='Salir', command=quit)
        # al box añadele el objeto tk (boton creado=bt)
        box.add_tk_widget(bt)
        
        raiz.display()
        
# Ejecutamos la apliacion
mi_app = Aplicacion()