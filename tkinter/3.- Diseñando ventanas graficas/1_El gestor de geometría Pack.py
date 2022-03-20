'''Creacion de ventanas con gestor de geometría (pack)'''


#!usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import ttk, font
import getpass
# Muchos programas que interactúan con el usuario a través de la terminal necesitan preguntar al usuario valores
# de contraseña sin mostrar lo que escribe el usuario la pantalla. El módulo getpass proporciona una forma portátil
# de manejar tales solicitudes de contraseña de forma segura.
# La función getpass() imprime un mensaje, luego lee la entrada del usuario hasta que presione retorno. La entrada
# se devuelve como una cadena al que la llama. p=getpass.getpass()
# En este programa usamos getpass.getuser() para poner el nombre del usuario del sistema en la primera caja de texto.

class Aplicacion():
    def __init__(self):
        self.raiz = Tk()
        self.raiz.title("Acceso")
        
        # Cambia el formato de la fuente actual a negrita para
        # resaltar las dos etiquedas que acompañan a las cajas
        # de entrada.  (Para este cambio se ha importado el
        # módulo 'font' al comienzo del programa):
        
        fuente = font.Font(weight='bold')
        
        # Define las etiquetas que acompañan a las cajas de
        # entrada y asigna el formato de fuente anterior:
        
        self.etiq1 = ttk.Label(self.raiz, text="Usuario", font=fuente)
        self.etiq2 = ttk.Label(self.raiz, text="Contraseña", font=fuente)
        
        
        # En tkinter puedes preguntar al sistema que te diga cuando
#         una variable ha cambiado, (esto se llama tracing) y sirve
#         para actualizar ciertos widgets cuando se modifica una
#         variable asociada. No hay forma de detectar cambios en las
#         variables en python pero tkinter si te lo permite.
#         Los metodos son:
#             var = StringVar() para declarar la variable
#             var.set("hello") para establecer el valor de la variable
#             var.trace("w", callbak) puede usar el metodo trace para observar las
#             llamadas (callbacks) a las variables
#             var.get() para obtener el valor actual de la variable.
        # Declara dos variables de tipo string para contener
        # al usuario y la contraseña:
        
        self.usuario = StringVar()
        self.clave = StringVar()
        
        # Realiza una lectura del nombre de usuario que
        # inición sesión en el sistema y lo asigna a la variable
        # 'self.usuario' (Para capturar esta información se ha importado
        # el módulo getpass al comienzo del programa):
        
        self.usuario.set(getpass.getuser())
        
        # Define dos cajas de entrada que aceptarán cadenas
        # de una longitud máxima de 30 caracteres.
        # A la primera de ellas 'self.ctext1' que contendrá
        # el nombre del usuario, se le asigna la variable
        # 'self.usuario' a la opción'textvariable'. Cualquier
        # valor que tome la variable durante la ejecución del programa
        # quedará reflejada en la caja de entrada.
        # En la segunda caja de entrada, la de la contraseña,
        # se hace lo mismo. Además, se establece la opción
        # 'show' con un "*" para ocultar la escritura
        # de las contraseñas:
        
        self.ctext1 = ttk.Entry(self.raiz,textvariable=self.usuario,width=30)
        self.ctext2 = ttk.Entry(self.raiz,textvariable=self.clave,width=30, show="*")
        # Pone una barra horizontal para separar los widgets.
        self.separ1 = ttk.Separator(self.raiz, orient=HORIZONTAL)
        
#         Se definen dos botones con dos métodos: El botón
#         'Aceptar' llamará al método 'self.aceptar'; y el botón
#         'Cancelar' finalizará la aplicación si se llega a
#         presionar.

        self.boton1 = ttk.Button(self.raiz, text="Aceptar",command=self.aceptar)
        self.boton2 = ttk.Button(self.raiz, text="Cancelar", command=quit)
        
#       Se definen las posiciones de los widgets dentro de
#       la ventana. Todos los controles se van colocando
#       hacia el lado de arriba, excepto, los dos últimos,
#       los botones, que se situarán debajo del último 'TOP':
#       el primer botón hacia el lado de la izquierda y el
#       segundo a su derecha.
#       Los valores posibles para la opción 'side' son :
#       TOP (arriba), BOTTOM (abajo), LEFT (izquierda) y  RIGHT (derecha).
#       Si se omite, el valor será TOP.
#           La opción 'fill' se utiliza para indicar al gestor
#       cómo expandir/reducir el widget si la ventana cambia
#       de tamaño. Tiene tres posibles valores: BOTH (AMBOS
#       horizontal y vertical), X (Horizontalmente) e Y (Verticalmente).
#       Funcionará si el valor de la opción 'expand' es True
        
        self.etiq1.pack(side=TOP,fill=BOTH, expand=True, padx=5, pady=5)
        self.ctext1.pack(side=TOP, fill=X, expand=False, padx=5,pady=5)
        self.etiq2.pack(side=TOP, fill=BOTH, expand=True,padx=5,pady=5)
        self.ctext2.pack(side=TOP, fill=X,expand=True,padx=5,pady=5)
        self.separ1.pack(side=TOP, fill=BOTH, expand=True,padx=5,pady=5)
        self.boton1.pack(side=LEFT, fill=BOTH, expand=True,padx=5,pady=5)
        self.boton2.pack(side=RIGHT, fill=BOTH, expand=True, padx=5,pady=5)
        
#         Cuando se inicia el programa se asigna el foco
#         a la caja de entrada de la contraseña para que se pueda
#         empezar a escribir directamente:
        
        self.ctext2.focus_set()
        
             
        self.raiz.mainloop()
        
#         El metodo 'aceptar' se emplea para validar la
#         contraseña introducida. Será llamada cuando se presione
#         el boton 'Aceptar'. Si la contraseña coincide
#         con la cadena 'Tkinter' se imprimirá el mensaje
#         'Acceso permitido' y los valores aceptados. En caso
#         contrario, se monstrará el mensaje 'Acceso denegado' y el foco
#         volverá la mismo lugar.
        
    def aceptar(self):
        if self.clave.get() =='herodoto':
            print("Acceso permitido")
            print("Usuario:   ", self.ctext1.get())
            print("Contraseña:", self.ctext2.get())
        else:
            print("Acesso denegado")
                
#                 Se inicializa la variable 'self.clave' para
#                 que el widget 'self.ctext2' quede limpio.
#                 Por ultimo, se vuelve a asignar el foco a
#                 este widget para poder escribir una nueva
#                 contraseña.
                
        self.clave.set("")
        self.ctext2.focus_set()

def main():
    mi_app = Aplicacion()
    return 0

if __name__=="__main__":
    main()
    
            
            

            
        

