from tkinter import *
from tkinter import ttk

# Crea una clase Python para definir el interfaz de usuario de
# la aplicación. Cuando se cree un objeto del tipo 'Aplicacion'
# se ejecutará automáticamente el método __init__() qué
# construye y muestra la ventana con todos sus widgets:


class Aplicacion():
    def __init__(self):
        raiz = Tk()
        raiz.geometry('300x200')
        raiz.configure(bg = 'beige')
        raiz.title('Aplicación')
        ttk.Button(raiz, text='Salir', command=raiz.destroy).pack(side=BOTTOM)
        raiz.mainloop()
        
# Define la funcion main() que es en realidad la que indica
# el comienzo del programa. Dentro de ella se crea el objeto
# aplicacion 'mi_app' basado en la clase 'Aplicacion':

def main():
    mi_app = Aplicacion()
    return 0

# Mediante el atributo __name__ tenemos acceso al nombre de un
# módulo. Python utiliza este atributo cuando se ejecuta
# un programa para conocer si el módulo es ejecutado de forma
# independiente (en este caso __name__ = '__main__' o es
# importado:       

if __name__ == '__main__':
    
    main()
    