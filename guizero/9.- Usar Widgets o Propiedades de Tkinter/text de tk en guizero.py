from guizero import App, Text
from tkinter import Message, HORIZONTAL, BOTH, TOP
from tkinter.ttk import Separator

app=App(title="My gui")
app.tk.geometry("300x200")

message=Text(app, text="A really long string that has too many characters to show up on one line within the default window size")
separador = Separator(app.tk, orient=HORIZONTAL)
separador.pack(side=TOP, fill=BOTH, expand=True,padx=5,pady=5)
msg2 = Message(app.tk, text="A really long string that has too many characters to show up on one line within the default window size")
msg2.pack()
app.display()