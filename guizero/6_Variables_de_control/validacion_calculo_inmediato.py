#!/usr/bin/var python
# -*- coding: utf-8 -*-
'''El programa de este ejemplo calcula el coste de un viaje en tren teniendo en cuenta el número
de viajeros; el tipo de billete (de sólo ida o de ida y vuelta); la clase en la cual se viaja (que
puede ser clase turista, primera o lujo); la distancia en kilómetros y el precio por kilómetro (por
defecto es 0,10 céntimos de euro).
El cálculo del importe a pagar se realiza multiplicando número de viajeros por km y precio, con
los siguientes incrementos:
Si el viaje es de ida y vuelta se multiplica el total por 1,5
Si la clase es primera se multiplica el total por 1,2 y si es de lujo se multiplica por 2
y DE MANERA INMEDIATA

En GUIZERO  solo hace falta incorporar al widget la propiedad command=
incluso con el spinbox de tkinter'''
#no hemos tenido que definir ninguna variable de control.


from guizero import *
from tkinter import Spinbox, HORIZONTAL, IntVar
from tkinter.ttk  import Separator



def calculo():
    # Este diccionario se usa para asignar el valor en funcion de la eleccion del ButtonGroup clase.
    clase_dict={"Turista":1, "Primera":1.5, "Lujo":2}
    p_clase=clase_dict[clase.value]
    # ida_vuelta se usa para asignar el valor de 1 si el checkbotton no esta seleccionado = 0, o el valor
    # de 1.5 si este esta seleccionado y su valor es de 1
    ida_vuelta = 1 if idavu.value==0 else 1.5
    # Calcula el total que se mostrara en el cuadro de texto resultado
    total = num_via.get() * ida_vuelta * p_clase * (int(dist.value) * float(coste.value))
    resultado.value=f'{total:0.2f} €' # minimo 0 posiciones enteras y 2 decimales.
   

raiz=App(title="Alta Velocidad       ", width=220)

# Importamos la imagen con el metodo Picture
Picture(raiz, "bus.png")

# Creamos una caja extendida y alargada a la izquierda para que haga de margen
box_padx=Box(raiz, align='left', width=10, height='fill')
# A la derecha creamos otra caja que contendran al resto de elementos salvo a los botones
box=Box(raiz, width='fill', height='fill', align='right', layout='grid') # Posiciona a los widgets mediante grid

Text(box, text="Viajeros:", grid=[0,0], align='left')

# Como un objeto Spinbox no existe en guizero tengo que importarlo de tkinter.
# El parametro wrap=False hace que cuando llega a 20 no vuelva a empezar a 1. En True volveria a 1
# al llegar a 20.
# El parametro state='readonly' hace que no se pueda escribir dentro
# texvariable contendra la variable de control que repondera antre cualquier cambio que se haga en el objeto

num_via = IntVar(value=1) # Creamos la variable de control de tipo Entero y le asignamos para empezar le valor de 1
# lo hacemos de esta forma porque al no ser spinbox un objeto de guizero no admite la propiedad value
viaje=Spinbox(box.tk, from_=1, to=20, wrap=False, textvariable=num_via, state='readonly', command=calculo)
viaje.grid(column=0, row=1, padx=5, pady=5)

idavu=CheckBox(box, text='Ida y vuelta', grid=[0,2], align='left', command=calculo)

Text(box, text="Clase:", grid=[0,3], align='left')
clase=ButtonGroup(box, options=["Turista", "Primera", "Lujo"], selected="Turista", grid=[0,4], align='left', command=calculo)


Text(box, text="Distancia en Km.", grid=[0,5], align="left")
dist=TextBox(box, grid=[0,6], width=20, command=calculo)
dist.value=1

Text(box, text="Precio:", grid=[0,7], align='left')
coste=TextBox(box, grid=[0,8], width=20, command=calculo)
coste.value=0.10

Text(box, text="A pagar en Euros: ", align='left', grid=[0,9])
# Para poder crear un cuadro de texto con fondo negro y letras de texto en verde,
# - con el cuadro de texto alineado a la derecha- la unica forma en guizero
# es crear una caja box3 y luego meter dentro un cuadro de texto alineado a la derecha.
box3=Box(box, grid=[0,10], width=165, height=25)
box3.bg='black'
resultado = Text(box3, align="right", bg='black', color="#03f943", text="0.0")

separ=Separator(box.tk, orient=HORIZONTAL)
esp_h=Text(box, text="", grid=[0,11], height=1) # Solo para meter un espacio.
separ.grid(column=0, row=12, sticky="ew") # Creo que tb se puede utilizar separ.config(Para modificar los parametros del objeto)

# Definimos los botones de Calcular y salir de la ventana dentro de una caja que es box4
box4=Box(box, grid=[0,13], width='fill', height='fill')
Text(box4, text="",align="top") # lo unico que hace es poner un espacio para bajar un poco los botones
# boton1=PushButton(box4, text="Calcular", align='left', padx=10, pady=5, command=calculo)
Text(box4, text="",align="left")
boton1=PushButton(box4, text="Salir", align='right', padx=80, pady=5, command=quit)

calculo()

raiz.display()
