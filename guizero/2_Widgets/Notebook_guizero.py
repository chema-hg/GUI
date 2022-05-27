from guizero import App, Box
from tkinter import ttk
from tkinter.ttk import Notebook

# set up app to use grid layout
app = App(title="Uso de ttk Notebook", layout="grid")

# set up box to use grid and place it in app at 0,0
box = Box(app, border=True, layout='grid', grid=[0,0])

# create a notebook
nb = Notebook(box.tk)

# create some frames for the tabs
pestana_a = ttk.Frame(nb)
pestana_b = ttk.Frame(nb)

# add the tabs
nb.add(pestana_a, text='Pestaña A')
nb.add(pestana_b, text='Pestaña B')

# important - add tk widget only after it is completed
box.add_tk_widget(nb, grid=[0,0])


app.display()