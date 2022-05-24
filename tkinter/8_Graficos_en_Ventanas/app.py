# librerias de gráficos normales
import tkinter as tk
# librerias para insertar el gráfico
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# Libreria para crear el gráfico
import matplotlib.pyplot as plt

# Creamos la ventana y el contenedor "frame" que contendrá el gráfico.
ventana = tk.Tk()
ventana.geometry('300x250')
ventana.title("Gráfica insertada en tkinter")
frame = tk.Frame(ventana, bg='yellow')
frame.grid(column=0, row=0, sticky='nsew')

#Diseño del gráfico
mascotas = [12, 9, 3, 1]
nombres = ["perros", "gatos", "peces", "tortugas"]

fig, axs = plt.subplots(dpi=80, figsize=(4, 3))
fig.suptitle("Grafico Principal")

axs.bar(nombres, mascotas)

# Dibujamos el gráfico dentro del frame definido usando
# un Canvas de tkinter.
canvas = FigureCanvasTkAgg(fig, master=frame)
canvas.draw()
canvas.get_tk_widget().grid(column=0, row=0)

# Renderizamos la ventana.
ventana.mainloop()