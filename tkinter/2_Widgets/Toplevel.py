from tkinter import *
 
def NuevaVentana():
    window = Toplevel()
    window.geometry('150x150')
    newlabel = Label(window, text = "Settings Window")
    newlabel.pack()
 
 
root = Tk()
root.geometry('200x200')
 
myframe = Frame(root)
myframe.pack()
 
mybutton = Button(myframe, text = "Settings", command = NuevaVentana)
mybutton.pack(pady = 10)
 
root.mainloop()