from tkinter import *
from tkinter.filedialog import askopenfile, askopenfilename
# Diálogo de directorio estándar
from tkinter.filedialog import askdirectory


print(askopenfilename(title='Abrir archivo', initialdir="/home/chema",
                      filetypes=[('All files', '*'),('jpeg files', '*.jpg')]))
