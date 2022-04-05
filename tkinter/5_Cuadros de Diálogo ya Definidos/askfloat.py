from tkinter import *
from tkinter.simpledialog import askfloat

raiz=Tk()
# .withdraw() oculta la ventana.
raiz.withdraw()
print(askfloat('Entry', 'Introduce un número: '))