#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import ttk, font
import getpass

'''Gestor de geometría (grid). Ventana dimensionable'''


class Aplicacion():

    def __init__(self):
        self.raiz = Tk()
        self.raiz.title("Acceso")
         
        fuente = font.Font(weight='bold')

#     Define un widget de tipo 'Frame' (caja o marco) que será el
#     contenedor del resto de widgets. El marco se situará
#     en la venta 'self.raiz' ocupando toda su extensión.
#     El marco se define con un borde de 2 pixeles y la opción
#     'relief' con el valor 'raised' (elevado) añade
#     un efecto 3D a su borde.
#     La opción 'relief' permite los siguientes valores:
#         FLAT (llano), RAISED (elevado), SUNKEN (hundido),
#         GROOVE (hendidura) y RIDGE (borde elevado).
#         La opciópn 'padding' añade espacio extra interior para
#         que los widgets no queden pegados al borde del marco.

        self.marco = ttk.Frame(self.raiz, borderwidth=2,
                               relief='raised', padding=(10,10))

#         Define el resto de widgets pero en este caos el primer
#         parámetro indica que se situarán en el widget del marco
#         anterior 'self.marco'.

        self.etiq1 = ttk.Label(self.marco, text="Usuario:",
                               font=fuente, padding=(5,5))
        self.etiq2 = ttk.Label(
            self.marco, text="Contraseña:", font=fuente, padding=(5,5))

#         Define variables para las opciones 'textvariable' de
#         cada caja de entrada 'ttk.Entry()'.

        self.usuario = StringVar()
        self.clave = StringVar()
        self.usuario.set(getpass.getuser())
        self.ctext1 = ttk.Entry(
            self.marco, textvariable=self.usuario, width=30)
        self.ctext2 = ttk.Entry(self.marco, textvariable=self.clave, show="*", width=30)
        self.separ1 = ttk.Separator(self.marco, orient=HORIZONTAL)
        self.boton1 = ttk.Button(self.marco, text="Aceptar", padding=(5,5), command=self.aceptar)
        self.boton2 = ttk.Button(
            self.marco, text="Cancelar", padding=(5, 5), command=quit)

        # Define la ubicación de cada widget en el grid.
        # En este ejemplo en realidad hay dos grid (cuadrículas):
        # Una cuadrícula de 1fx1c que se encuentra en la ventana 
        # que ocupará el Frame; y otra en el Frame de 5fx3c para
        # el resto de controles.
        # La primera fila y primera columna serán la número 0.
        # La opción 'column' indica el número de columna y la
        # opción 'row' indica el número de fila donde hay que 
        # colocar un widget. 
        # La opción 'columnspan' indica al gestor que el 
        # widget ocupará en total un número determinado de
        # columnas. Las cajas para entradas 'self.ctext1' y
        # 'self.ctext2' ocuparán dos columnas y la barra
        # de separación 'self.separ1' tres.
        
        #IMPORTANTE--------------------------------------------------------------------------------
        # Para conseguir que la cuadricula y los widgets se 
        # adapten al contenedor, si se amplia o reduce el tamaño
        # de la ventana, es necesario definir la opción 'sticky'.
        # Cuando un widget se ubica en el grid se coloca en el
        # centro de su celda o cuadro. Con 'sticky' se
        # establece el comportamiendo 'pegajoso' que tendrá el 
        # widget dentro de su celda, cuando se modifique la 
        # dimensión de la ventana. Para ello, se utilizan para
        # expresar sus valores los puntos cardinales: N (Norte),
        # S (Sur), (E) Este y (W) Oeste, que incluso se pueden
        # utilizar de forma combinada. El widget se quedará 
        # 'pegado' a los lados de su celda en las direcciones
        # que se indiquen. cuando la ventana cambie de tamaño. 
        # Pero con definir la opción 'sticky' no es suficiente: 
        # hay activar esta propiedad más adelante.

        self.marco.grid(column=0, row=0, sticky=(N,S,E,W))
        self.etiq1.grid(column=0, row=0, sticky=(N,S,E,W))
        self.ctext1.grid(column=1, row=0, columnspan=2, sticky=(E,W))
        self.etiq2.grid(column=0, row=1, sticky=(N,S,E,W))
        self.ctext2.grid(column=1, row=1, columnspan=2, sticky=(E,W))
        
        #The separator has a natural width of 1 pixel. You told it to reserve the space across 3 columns,
        #but you haven't requested that the separator actually fill those 3 columns. To solve this, supply
        #the sticky attribute, which says "if there's more space than needed for this widget, make the edges
        #of the widget "stick" to specific sides of its container".

        #In this case, you want the separator to sticky to the left and right edges of it's container.
        #The sticky attributes uses the points of the compass for values, so you want "e" for east, and "w" for west:

        #ttk.Separator(...).grid(..., sticky="ew")
        self.separ1.grid(column=1, row=3, columnspan=3, sticky="nsew")
        
        self.boton1.grid(column=1, row=4,sticky=(E))
        self.boton2.grid(column=2, row=4,sticky=(W))
        
        # A continuación, se activa la propiedad de expandirse
        # o contraerse definida antes con la opción
        # 'sticky' del método grid().
        # La activación se hace por contenedores y por filas
        # y columnas asignando un peso a la opción 'weight'.
        # Esta opción asigna un peso (relativo) que se utiliza
        # para distribuir el espacio adicional entre columnas
        # y/o filas. Cuando se expanda la ventana, una columna
        # o fila con un peso 2 crecerá dos veces más rápido
        # que una columna (o fila) con peso 1. El valor
        # predeterminado es 0 que significa que la columna o
        # o fila no crecerá nada en absoluto. 
        # Lo habitual es asignar pesos a filas o columnas donde 
        # hay celdas con widgets.
        
        # Establecemos los pesos por cada contenedor.
        self.raiz.columnconfigure(0, weight=1)
        self.raiz.rowconfigure(0, weight=1)
        
        self.marco.columnconfigure(0, weight=1)
        self.marco.columnconfigure(1, weight=1)
        self.marco.columnconfigure(2, weight=1)
        self.marco.rowconfigure(0, weight=1)
        self.marco.rowconfigure(1, weight=1)
        self.marco.rowconfigure(4, weight=1)

        # Establece el foco en la caja de entrada de la contraseña

        self.ctext2.focus_set()
        self.raiz.mainloop()

    def aceptar(self):
        if self.clave.get()=='tkinter':
            print('Acceso Permitido')
            print('Usuario:    ', self.ctext1.get())
            print('Contraseña: ', self.ctext2.get())
        else:
            print('Acceso denegado')
            self.clave.set("")
            self.ctext2.focus_set()

def main():
    mi_app = Aplicacion()
    return 0

if __name__=='__main__':
    main()

