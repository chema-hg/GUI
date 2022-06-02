from guizero import App, Box, Text
from tkinter import Spinbox, ttk
from tkinter.ttk import Progressbar, Notebook

app = App(title="Using tk widgets", width=300, height=200)

Text(app, text="Spinbox")

# add a spinbox widget to the app
sp = Spinbox(from_=0, to=10)
app.add_tk_widget(sp)

Text(app, text="and Progressbar")

box = Box(app, border=True)

# add a progress bar to the box
pb = Progressbar(box.tk)
box.add_tk_widget(pb)
pb.start()

Text(app, text="in guizero")

box1 = Box(app, border=True)
nb = Notebook(box1.tk)
# create some frames for the tabs
signal_page_inputs = ttk.Frame(nb)
signal_page_outputs = ttk.Frame(nb)

# add the tabs
nb.add(signal_page_inputs, text='Signal Inputs')
nb.add(signal_page_outputs, text='Signal Outputs')

# important - add tk widget only after it is completed
box1.add_tk_widget(nb)

app.display()