from guizero import *
from tkinter import *
from tkinter.ttk import Button


raiz=App(title="Aplicación", bg='beige', width=300, height=200)

box = Box(raiz, border=True, align='bottom')
bt1 = Button(box.tk,text='Salir', command=quit)
box.add_tk_widget(bt1)

raiz.display()
