from tkinter import *
 
def set():
    print("Hola Mundo")
 
root = Tk()
root.geometry("200x150")
 
frame = Frame(root)
frame.pack()
button = Button(frame, text = "Botón1", command = set,
                fg = "red", font = "Verdana 14 underline",
                bd = 2, bg = "light blue", relief = "groove")
button.pack(pady = 5)
 
root.mainloop()