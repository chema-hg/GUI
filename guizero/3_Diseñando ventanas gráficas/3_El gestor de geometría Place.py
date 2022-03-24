from guizero import *
''' SUPER IMPORTANTE: PARA QUE FUNCIONE LA GEOMETRIA PLACE HAY QUE PONER visible=False en todos
los WIDGETS DE GUIZERO QUE QUERAMOS POSICIONAR. ES COMO SI DIJERAN OCULTALOS QUE YA LOS PONGO YO'''
''' LOS WIDGET IMPORTADOS DE TKINTER.TTK EL METODO SE PONE COMO EN TKINTER EJ SEPAR1.PLACE() Y NO SEPAR1.TK.PLACE'''
from tkinter import HORIZONTAL, OUTSIDE
from tkinter.ttk import Separator
from getpass import getuser

def aceptar():
    if ctext2.value == 'herodoto':
        print('Acceso Permitido')
        print('Usuario:    ', ctext1.value)
        print('Contraseña: ', ctext2.value)
        ctext2.value="" #Borra el contenido del 2º cuadro de texto
        etiq3.text_color="blue"
        etiq3.value="Acceso Permitido"
        #quit() #Sale del programa
    else:
        print('Acceso denegado')
        etiq3.text_color="red"
        etiq3.value="Acceso Denegado"
                
def haz_esto():
    print('haz esto')
    ctext2.value=""
    etiq3.value=""

usuario = getuser()


raiz = App(title='Acceso', width=430, height=200)
raiz.tk.resizable(0,0) # Para inmovilizar la ventana equivale a resizable(width=False,height=False)

etiq1 = Text(raiz, text="Usuario:", visible=False)
etiq1.tk.place(x=30, y=40)
ctext1 = TextBox(raiz, width=30, visible=False)
ctext1.tk.place(x=150, y=42)
ctext1.value = usuario
etiq2 = Text(raiz, text="Contraseña:", visible=False)
etiq2.tk.place(x=30, y=80)
ctext2 = TextBox(raiz, width=30, visible=False)
ctext2.tk.place(x=150, y=80)
# Permite ocultar el texto tecleado True=* otro caracter se pone y ya esta.
ctext2.hide_text="#"
ctext2.when_clicked= haz_esto


etiq3=Text(raiz, text="", visible=False)
etiq3.tk.place(x=150, y=120)

separ1 = Separator(raiz.tk, orient=HORIZONTAL)
separ1.place(x=5, y=145, bordermode=OUTSIDE, height=10, width=420)
boton1 = PushButton(raiz, text="Aceptar", visible=False, padx=10, pady=5, command=aceptar)
boton1.tk.place(x=170, y=160)
boton2 = PushButton(raiz, text="Cancelar", visible=False, padx=10, pady=5, command=quit)
boton2.tk.place(x=290, y=160)

ctext2.focus()
raiz.display()