''' Cuadro de diálogo standard '''

from tkinter import *
from tkinter.messagebox import *

def callback():
    if askyesno('Confirmación', '¿Estás seguro de que quieres salir?'):
        showwarning('Si', 'Salir aún no esta implementado')
    else:
        showinfo('No', 'Salir ha sido cancelado')

msg_error = '¡Lo siento, no se permite el Spam!'
Button(text='Salir', command=callback).pack(fill=X)
Button(text='Spam', command=lambda: showerror('Error', msg_error)).pack(fill=X)
mainloop()