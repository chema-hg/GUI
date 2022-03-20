from guizero import *
import getpass

# Todo la explicacion esta en el archivo homonimo en tkinter puro "El gestor de geometria Pack"

def aceptar():
    clave = ctext2.value # Asigna a la variable clave el value que tenda el objeto ctext2
    
    if clave == 'herodoto':
        print('Acceso Permitido')
        print('Usuario: ', usuario)
        print('Contraseña', clave)
    else:
        print('Accesos Denegado')
        ctext2.value = ""
        

usuario = getpass.getuser()


raiz = App(title='Acceso', width=255, height=170)
# SI NO QUISIERAMOS QUE SE PUDIERA MODIFICAR EL TAMAÑO DE LA VENTANA.
raiz.tk.resizable(width=False, height=False)

# Diseñamos los diferentes widgets.

box3 = Box(raiz, width="fill",height="fill")
#font= permite elegir una fuente instalada en el sistema
etiq1 = Text(box3, text="Usuario", align="left", font='padmaa-Bold.1.1')
# width or height ='fill' Expande todo el objeto dentro de la ventana
ctext1 = TextBox(raiz, width='fill')
ctext1.value=getpass.getuser()

box4 = Box(raiz, width="fill",height="fill")
etiq2 = Text(box4, text="Contraseña", align="left", font='padmaa-Bold.1.1')
ctext2 = TextBox(raiz, width='fill', hide_text=True)
ctext2.focus()

# Como no encontre el objeto Separator de tkk he usado Drawing en su lugar.
# para dibujar una recta dentro de un box que haga de separador.
box10=Box(raiz, width='fill', height=11, visible=True, border=0)
recta1 = Drawing(box10, align='left', width='fill')
recta1.line(0,6,1000,6, color='grey')


bt1 = PushButton(raiz,text='Aceptar', command=aceptar, align='left', padx=5,pady=5, width='fill', height='fill')
bt2 = PushButton(raiz,text='Cancelar', command=quit, align='right', padx=5,pady=5, width='fill', height='fill')

raiz.display()

