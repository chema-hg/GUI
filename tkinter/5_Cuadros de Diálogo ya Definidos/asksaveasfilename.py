from tkinter import *
from tkinter.filedialog import asksaveasfilename


print(asksaveasfilename(initialdir="/", title="Guardar Archivo", 
                    filetypes=[("jpeg files", "*.jpg"), ("all files", "*.*")]))
