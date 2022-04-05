from tkinter import *
from tkinter.simpledialog import askstring

raiz=Tk()
# .withdraw() oculta la ventana.
raiz.withdraw()
print(askstring('Entry', 'Introduce una frase: '))