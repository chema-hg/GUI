from guizero import *


# Retornan True o False.
print(messagebox.askyesno(message="¿Desea continuar?", title="Título"))
print(messagebox.askokcancel(message="¿Desea continuar?", title="Título"))
print(messagebox.askretrycancel(message="¿Desea reintentar?", title="Título"))