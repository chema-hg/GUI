from tkinter import *
from tkinter.simpledialog import askinteger

raiz=Tk()
# .withdraw() oculta la ventana.
raiz.withdraw()
print(askinteger('Entry', 'Introduce un número: '))