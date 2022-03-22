#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from guizero import *

#HORIZONTAL is Tkinter's variable. If you want to use it you have to import it or have to use like Tkinter.HORIZONTAL
#If you dont want to add Tkinter then you can do from Tkinter import HORIZONTAL
from tkinter import HORIZONTAL
# CUALQUIER VARIABLE DE TK QUE NO APAREZCA HAY QUE IMPORTARLA. 
from tkinter.ttk import Separator #Importamos el widget que necesitemos de ttk 
from getpass import getuser

def aceptar():
        
        if ctext2.value == 'herodoto':
            print('Acceso Permitido')
            print('Usuario:   ', ctext1.value)
            print('Contraseña: ', ctext2.value)
            ctext2.value="" #Borra el contenido del 2º cuadro de texto
            quit() #Sale del programa
        else:
            print('Acceso denegado')
            ctext2.value="" # Borra el contenido del 2º cuadro de texto si se falla.

usuario = getuser() # Captura el nombre del usuario que usa el sistema.
            

raiz = App(width=390, height=120, title="Acceso")
raiz.tk.resizable(0, 0) # Es otra forma de decirle que la ventana es fija y no se puede cambiar el tamaño.

marco_sup = Box(raiz) # Creamos un marco con un gestor de geometria grid (por celdas)
Text(marco_sup, text="", size=5) # Pongo esto para separar lo siguiente del borde superior.

marco = Box(raiz, layout="grid") # el marco usara (3 colum x 5 filas) grid.
# el tamaño de cada celda viene determinado por lo que contiene dentro. 

etiq1 = Text(marco, text="Usuario", grid=[0, 0], align='left', font='padmaa-Bold.1.1', size=14)
ctext1 = TextBox(marco, grid=[1, 0, 2, 1], width=30, align='left') # lo alineamos a la izquierda dentro del grid.
etiq1 = Text(marco, text="Contraseña", grid=[0, 1], align='left', font='padmaa-Bold.1.1', size=14) # size es el tamaño de la letra
ctext2 = TextBox(marco, grid=[1, 1, 2, 1], width=30, hide_text=True) # hide_text=True cambia las letras por *
# grid=[1,1,2,1] situa el grid en la columna 1 y fila 1 y luego lo expande 1 columnas y 0 fila (sumamos 1 a lo q queremos expandir)
# El grid no admite [1,1,0,0], xq por defecto  el grid [1,1] es como si fuera [1,1,1,1]
#x lo que expandir una columna seria [1,1,2,1] o expandir una fila [1,1,1,2]
#------------------------------------------------------------------------------------------

separ1 = Separator(marco.tk, orient=HORIZONTAL)
separ1.grid(column=1, row=3, columnspan=3, sticky="ew")
'''Para que un widget de tk o ttk funcione en guizero hay que diseñarlo y luego pack o grid o el gestor de
geometria que se use'''
#--------------------------------------------------------------------------------------------
boton1 = PushButton(marco, grid=[1, 4], text='Aceptar', padx=16, pady=6, command=aceptar)
boton2 = PushButton(marco, grid=[2, 4], text='Cancelar', padx=16, pady=6, command=quit)

ctext1.value=usuario
ctext2.focus() # Pone el foco en el cuadro 2 donde pondremos la contraseña.


raiz.display()
