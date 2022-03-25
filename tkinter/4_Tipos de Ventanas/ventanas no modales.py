#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''ejemplo de ventanas no modales porque mientras existen es posible interactuar libremente con ellas,
con ellas, sin ningún límite, excepto que si cerramos la ventana principal se cerrarán todas
las ventanas hijas abiertas.'''

from tkinter import *
from tkinter import ttk

class Aplicacion():
    
    # Declara una variable de clase para contar ventanas
    
    ventana = 0
    
    # Declara una variable de clase para usar en el
    # calculo de la posicion de la ventana
    
    posx_y = 0
    
    # Declara una ventana de aplicación
    
    def __init__(self):
        
        self.raiz=Tk()
        
        # Define la dimensión de la ventana 300x200
        # que se situara en la coordenada x=500, y=50
        
        self.raiz.geometry('300x200+500+50')
        
        self.raiz.resizable(0,0)
        self.raiz.title("Ventana de aplicación")
        
        # Define botón 'Abrir' que se utilizará para
        # abrir las ventanas de diálogo. El botón
        # está vinculado con el método 'self.abrir'
        
        boton = ttk.Button(self.raiz, text="Abrir", command=self.abrir)
        boton.pack(side=BOTTOM, padx=20, pady=20)
        self.raiz.mainloop()
        
    def abrir(self):
        ''' Construye una ventana de dialogo '''
        
        # Define una nueva ventana de diálogo
        
        # Las ventanas de dialogo hijas se definen con TopLevel()
        self.dialogo = Toplevel()
        
        # incrementa en 1 el contador de ventanas
        # en la variable de clase a la que se puede acceder
        # desde cualquier metodo de la clase con la notación
        # del punto.
        Aplicacion.ventana+=1
        
        # Recalcula la posición de la ventana


        Aplicacion.posx_y += 50
        # el \ al final de la linea era para hacer un salto y que siga leyendo el codigo
        tamypos ='200x100+'+str(Aplicacion.posx_y)+ \
                  '+'+ str(Aplicacion.posx_y)
        print(tamypos)
        self.dialogo.geometry(tamypos)
        self.dialogo.resizable(0,0)
        
        # obtiene el identificador de la nueva ventana
        
        ident = self.dialogo.winfo_id()
        
        # Construye el mensaje de la barra de titulo
        
        titulo = str(Aplicacion.ventana)+": "+str(ident)
        print(titulo)
        self.dialogo.title(titulo)
        
        # Define el boton 'Cerrar' que cuando sea presionado
        # cerrara (destruira) la ventana 'self.dialogo' llamando
        # al metodo 'self.dialogo.destroy'
        
        boton = ttk.Button(self.dialogo, text='Cerrar', command=self.dialogo.destroy)
        boton.pack(side=BOTTOM, padx=20,pady=20)
        
        # Cuando la ejecución del programa llega a este
        # punto se utiliza el método wait.window() para
        # esperar que la ventana 'self.dialogo' sea
        # destruida.
        
        # Mientras tanto se atiende a los eventoso locales
        # que se produzcan, por lo que otras partes de la
        # apliación seguirán funcionando con normalidad.
        # Si hay codigo despues de esta linea se ejecutara
        # cuando la ventana 'self.dialogo' sea cerrada.
        
        self.raiz.wait_window(self.dialogo)
        
def main():
    mi_app = Aplicacion()
    return 0

if __name__=='__main__':
    main()
        
    
        
        
    