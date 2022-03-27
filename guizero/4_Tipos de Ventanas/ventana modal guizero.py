#!/usr/bin/var python
# -*- coding: utf-8 -*-

from guizero import *
# Las listas de un solo elemento tienen que tener una coma ,
# despues del elemento.
contador=[0,]
posx_y=[0,]

def dialogo():
    # En vez de variables globales (enteros, tuplas) vamos a utilizar listas que se modifican
    # por si solas a nivel global de la aplicacion.
    contador[0]=contador[0]+1
    posx_y[0]=posx_y[0]+50
    ventana=Window(raiz)
    ident = ventana.tk.winfo_id()
    ventana.title=f"{contador[0]} :{ident}"
    ventana.hide()
    ventana.tk.resizable(0,0)
    dimension = f"200x100+{posx_y[0]}+{posx_y[0]}"
    ventana.tk.geometry(dimension)
    #-----------------------------------------------------------------------
    PushButton(ventana, text="Cancelar", align="bottom", command=ventana.destroy)
     # Convierte la ventana ''self.dialogo' en
        # transitoria con respecto a su ventana maestra
        # 'self.raiz'.
        # Una ventana transitoria siempre se dibuja sobre
        # su maestra y se ocultará cuando la maestra sea
        # minimizada. Si el argumento 'master' es
        # omitido el valor, por defecto, será la ventana
        # madre
    ventana.tk.transient(master=raiz.tk)
    # El método grab_set() asegura que no haya eventos
        # de ratón o teclado que se envien a otra ventana
        # diferente a 'self.dialogo'. Se utilizará para
        # crear una ventana de tipo modal que será
        # necesario cerrar para poder trabajar con otra
        # diferente. Con ello, también se impide que la
        # misma ventana se abra varias veces.
    ventana.tk.grab_set()
    ventana.show()

raiz=App(title="Ventana de Aplicación")
raiz.tk.geometry("300x200+500+50")
raiz.tk.resizable(0,0)

boton=PushButton(raiz, text="Abrir", padx=20, pady=5, align="bottom", command=dialogo)
boton.tk.pack(pady=20)

raiz.display()