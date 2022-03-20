from tkinter import *
 
root = Tk()
root.geometry("200x150")
 
frame = Frame(root)
frame.pack()
 
var = StringVar()
var.set("Hola Mundo")
 
label = Label(frame, textvariable = var )
label.pack()
 
root.mainloop()