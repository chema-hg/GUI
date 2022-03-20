# Importa la libreria guizero
from guizero import *

class Aplicacion():
    # Definimos el constructor de la clase aplicacion.
    def __init__(self):
        
                                     
        # Definimos la ventana principal con su título, color de fondo, ancho, alto de la ventana principal.
        self.raiz = App(title='Aplicación', bg='beige', width=300, height=200)
        # Creamos un objeto boton
        # Texto, alineación abajo, distancia de las letras al x e y, comando del boton destruir la raiz.
        self.boton = PushButton(self.raiz, text='Salir', align='bottom', padx=25, pady=2, command=self.raiz.destroy)
        # Le asignamos el color de fondo inicial del boton
        self.boton.bg="#d9d9d9"
        # Vamos a definir un evento para cuando el raton entre en el boton lance
        # la funcion claro
        self.boton.when_mouse_enters=self.claro
        # Despues de definir todo, mostramos la aplicación
        self.raiz.display()       
        
    def claro(self):
            self.boton.bg="#ececec"
            #evento para cuando el raton sale del boton que vuelva la color normal
            self.boton.when_mouse_leaves=self.normal
        
    def normal(self):
            self.boton.bg="#d9d9d9"
        
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
    main() # Ejecuta la función que lanza el programa
    

     