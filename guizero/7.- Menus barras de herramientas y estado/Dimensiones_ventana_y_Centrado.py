from guizero import *

raiz = App()
W = 400 # ANCHO QUE QUERAMOS DE NUESTRA VENTANA
H = 400-30 # ALTO QUE QUERAMOS DE NUESTRA VENTANA

# CONSEGUIMOS EL ANCHO Y ALTO DE LA PANTALLA DEL ORDENADOR
ws = raiz.tk.winfo_screenwidth()
hs = raiz.tk.winfo_screenheight()

# CALCULAMOS LAS COORDENADAS X E Y DE LA VENTANA PARA QUE ESTE EN EL CENTRO
x = int((ws/2)-(W/2))
y = int((hs/2)-(H/2))

# ESTABLECEMOS LAS DIMENSIONES DE LA VENTANA Y DONDE TENEMOS QUE COLOCARLA
print(f'{W}x{H}+{x}+{y}')
raiz.tk.geometry(f'{W}x{H}+{x}+{y}')
raiz.width=W
raiz.height=H
raiz.title=('titulo') # Crea el titulo de la Ventana principal
#raiz.set_full_screen() # Muestra la ventana a pantalla completa, y sale pulsando Esc que es la tecla por defecto.
# Si quisieramos cambiar la tecla se pondria set_full_screen(tecla)
y=raiz.tk.winfo_height()
x=raiz.tk.winfo_width()
print(x, y)
#     Establece el VALOR MINIMO QUE TENDRA LA VENTANA (400,300)
#raiz.tk.minsize(400,300)


#     --------------------------- CAMBIA LA FUENTE O EL TAMAÑO DE LETRA DE LA VENTANA---------------------------
raiz.tk.option_add("*Font", "TkDefaultFont 11")
# Puedes cambiar la letra por defecto TkDefaultFont por otra pej. Helvetica, el numero
# el numero es el tamaño de la letra.

    
raiz.display()