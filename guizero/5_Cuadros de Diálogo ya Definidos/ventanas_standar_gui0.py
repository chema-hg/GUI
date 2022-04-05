''' Cuadro de diálogo standard con Guizero '''
# Importamos la librería Guizero
from guizero import *

def call_back():
    # Ventana de confirmación si o no
    if yesno('Confirmación', '¿Estás seguro de que quieres salir?'):
        # Ventana de advertencia
        warn('Si', 'Salir aún no esta implementado')
    else:
        # Ventana de información
        info('No', 'Salir ha sido cancelado')


raiz = App(height=100, width=60)


# Creamos una ventana principal con dos botones. (Salir y Error)
b1 = PushButton(raiz, command=call_back, text='Salir')
# Ventana de error
b2 = PushButton(raiz, text="Spam", command=lambda: raiz.error("Error", "¡Lo siento no se permite el Spam!"))

raiz.display()
