from tkinter import *
root = Tk()
root.geometry("200x220")
frame = Frame(root)
frame.pack()
 
label = Label(root,text = "Una lista de la compra.")  
label.pack()  
   
listbox = Listbox(root)  
   
listbox.insert(1,"Pan")  
listbox.insert(2, "Leche")  
listbox.insert(3, "Carne")  
listbox.insert(4, "Queso")
listbox.insert(5, "Verduras")  
   
listbox.pack()  
root.mainloop()