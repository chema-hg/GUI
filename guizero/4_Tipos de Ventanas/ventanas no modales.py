#!/usr/bin/var python
# -*- coding: utf-8 -*-
'''ejemplo de ventanas no modales porque mientras existen es posible interactuar libremente con ellas,
con ellas, sin ningún límite, excepto que si cerramos la ventana principal se cerrarán todas
las ventanas hijas abiertas.'''

from guizero import *

def dialogo():
    ''' Crea una nueva ventana de dialogo. Cada vez que se ejecuta se dibuja una
nueva ventana, con una nueva posicion y un nuevo titulo de ventana'''
    global ventana, posx_y
    # Incrementa en 1 el numero de ventanas abiertas
    ventana +=1
    # Incrementa en 50 los pixeles de la variable q controla la posicion
    posx_y +=50
    # variable de texto que contendra el tamaño y posicion de la ventana en geometry
    #tama_y_posc = "200x100"+"+"+str(posx_y)+"+"+str(posx_y)
    tama_y_posc = f"200x100+{posx_y}+{posx_y}"
    print(tama_y_posc)
        
    # En guizero se usa Window() para definir una ventana de dialogo.
    window = Window(raiz)
    # obtiene el identificador de la nueva ventana
    ident = window.tk.winfo_id()
    titulo = f"{ventana}:{ident}"
    print(ident)
    window.title=titulo
    window.hide()
    window.tk.geometry(tama_y_posc)
    window.tk.resizable(0,0)
    PushButton(window, text="Cancelar", align="bottom", command=window.destroy)
    window.show()

# Variable generica para contar las ventanas.
ventana = 0
# Variable generica para el calculo de la posición de la ventana
posx_y = 0

#---------------------------- Ventana Principal------------------------------------    
raiz = App(title="Ventana de Aplicación")
# La geometria del objeto raiz.tk es "(tamaño_x)x(tamaño_y)+posc_x+posc_y"
raiz.tk.geometry("300x200+500+50")
raiz.tk.resizable(0,0)

# En guizo el parametro padding afecta a la distancia del texto del boton
# respecto al borde del mismo, hace mas grande o mas pequeño al boton
boton = PushButton(raiz, text="Abrir", align="bottom", padx=20, pady=5, command=dialogo)

# Sin embargo si lo pones en el metodo tk afecta a la distancia al siguiente widget.
# En este caso a la distancia a la parte inferior de la ventana
boton.tk.pack(padx=20, pady=20)
#-----------------------------------------------------------------------------------


raiz.display()
