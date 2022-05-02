'''La aplicación de ejemplo utiliza imágenes de diferentes tamaños que se localizan en una carpeta llamada
"imagen". Estas imágenes son utilizadas en la barra de título, los submenús, la barra de herramientas y en
la ventana de diálogo "Acerca de" del submenú "Ayuda".'''

from guizero import *
from tkinter import PhotoImage,LEFT,RAISED
from tkinter import Menu, IntVar # Para crear el menu y Intvar (variable numerica) para la barra de estado.
import os, webbrowser, platform
# os lo usamos para el tema de directorios de los iconos
# webbrowser lo usamos para abrir una pagina web desde python
# platform para ver caracteristicas del sistema operativo en la barra de estado

'''PyRemoto: Acceso Remoto a equipos por ssh, sftp y rdp '''
   
__author__ = 'python para impacientes'
__title__= 'PyRemoto'
__date__ = ''
__version__ = '0.0.1'
__license__ = 'GNU GPLv3'


def Pyremote():           
    # CREA LA VENTANA DE INICIO Y COMO NOVEDAD VAMOS A PONERLA EN EL CENTRO DE LA PANTALLA
    global raiz
    raiz = App()
    W = 400 # ANCHO QUE QUERAMOS DE NUESTRA VENTANA
    H = 350 - 60 # ALTO QUE QUERAMOS DE NUESTRA VENTANA (60 es lo que ocupa la barra negra y la barra menu)
    
    # CONSEGUIMOS EL ANCHO Y ALTO DE LA PANTALLA DEL ORDENADOR
    ws = raiz.tk.winfo_screenwidth()
    hs = raiz.tk.winfo_screenheight()
    
    # CALCULAMOS LAS COORDENADAS X E Y DE LA VENTANA PARA QUE ESTE EN EL CENTRO
    x = int((ws/2)-(W/2))
    y = int((hs/2)-(H/2))
    
    # ESTABLECEMOS LAS DIMENSIONES DE LA VENTANA Y DONDE TENEMOS QUE COLOCARLA
    print(f'{W}x{H}+{x}+{y}')
    raiz.tk.geometry(f'{W}x{H}+{x}+{y}')
    raiz.title=(__title__+" "+__version__) # Crea el titulo de la Ventana principal
    #raiz.set_full_screen() # Muestra la ventana a pantalla completa, y sale pulsando Esc que es la tecla por defecto.
    # Si quisieramos cambiar la tecla se pondria set_full_screen(tecla)

#     Establece el VALOR MINIMO QUE TENDRA LA VENTANA (400,300)
    raiz.tk.minsize(400,290)
    icono1 = PhotoImage(file=iconos_app[0])
    raiz.tk.iconphoto(raiz, icono1) # Establece el icono 1 como icono de la aplicacion
    # aunque en ubuntu no aparece en la ventana solo aparece a la izquierda.
    
    
#     --------------------------- CAMBIA LA FUENTE O EL TAMAÑO DE LETRA DE LA VENTANA---------------------------
    raiz.tk.option_add("*Font", "TkDefaultFont 11")
    # Puedes cambiar la letra por defecto TkDefaultFont por otra pej. Helvetica, el numero
    # el numero es el tamaño de la letra.
    
    
#     ---------------------------------- BARRA DE MENU----------------------------------------------------
#     Esto seria la barra de menus en guizero pero es muy sencilla y queda mas fea
#     barra_menu = MenuBar(raiz,
#                   toplevel=["Sesiones", "Opciones", "Ayuda"],
#                   options=[
#                       [ ["Conectar", Sesiones_menu], ["Salir", lambda :quit()] ],
#                       [ ["Barra de Estado", Opciones_menu], ["Ssh", Opciones_menu], ["xterm", Opciones_menu], ["Thunar", Opciones_menu] ],                             
#                       [ ["Web", f_web], ["Atajos de Teclado", Ayuda_menu], ["Acerca de...",f_acerca]]
#                       ])
    
    barra_menu = Menu(raiz.tk) # Importamos Menu de tkinter y CREAMOS un objeto Menu.
    raiz.tk.config(menu=barra_menu) # asignamos ese objeto como menu de la raiz.
    
    # Ahora creamos los submenus
    sesiones_menu=Menu(barra_menu, tearoff=0)
    global opciones_menu #porque lo utiliza fuera de local la funcion f_cambiarop()
    opciones_menu=Menu(barra_menu, tearoff=0)
    ayuda_menu=Menu(barra_menu, tearoff=0)
    
    # ya tenemos los menus creados pero tenemos que asignar a la barra_menu los mismos.
    barra_menu.add_cascade(label="Sesiones", menu=sesiones_menu)
    barra_menu.add_cascade(label="Opciones", menu=opciones_menu)
    barra_menu.add_cascade(label="Ayuda", menu=ayuda_menu)
    #Bien ya tenemos nuestra barra con los 3 submenús funcionando bien, pero ocurre algo raro,
    #nos aparece una especie de elemento por defecto. Podemos hacer que desaparezca si indicamos
    #el parámetro tearoff=0 al definir los objetos submenus.
    
    #Vamos a añadir comandos de ejemplo en nuestros submenús:
    
    #------------------------------------- Submenu Sesiones (Primer Submenu) -----------------------------------------------
    
    icon_conectar=PhotoImage(file=iconos_app[1]) # Cargamos el miniicono para el submenu conectar
    sesiones_menu.add_command(label="Conectar...",
                              accelerator="Ctrl+c", underline=0,  
                              image=icon_conectar, compound=LEFT,
                              command=f_conectar)
                               # Si no pongo compound solo muestra el icono.
#     ACCELERATOR pone la tecla de acceso rapido y UNDERLINE subraya la primera letra de Label.
#     COMPOUND. Especifica si el widget debe mostrar texto y mapas/imágenes al mismo tiempo, y si es así,
#     donde el mapa de bits o imagen debe estar en relación con el texto. Debe ser uno de los valores:
#     “none”, “bottom”, “top”, “left”, “right”, o “center” Por defecto esta en none.                                                              # hay que poner el compound=LEFT
                                                                  
    sesiones_menu.add_separator() # La añadimos un bonito separador.
    
    icon_salir=PhotoImage(file=iconos_app[2])
    sesiones_menu.add_command(label="Salir",
                              accelerator="Ctrl+q", underline=0,
                              image=icon_salir, compound=LEFT,
                              command=quit) # le añadimos
    
    #------------------------------------- Submenu Opciones (segundo)------------------------------------------------
    global estado
    estado=IntVar(value=1) # varible numerica que recoje si el checkbutton esta pulsado o no. Por defecto le decimos
                        # que si aparezca pulsado. Se puede poner como estado.set(1)
    opciones_menu.add_checkbutton(label="Barra de Estado",
                                  variable=estado, onvalue=1, offvalue=0,
                                  command=barraEstado) # se activa o desactiva la barra de estado dependiendo si se
                                  # pulsa o no el checkbuttom
    
    
    opciones_menu.add_separator()
    
    # Los siguentes submenus los haremos con un radiobutton para que solo podamos seleccionar uno
    # de los tres
    global tipoConex
    tipoConex=IntVar(value=1)
    opciones_menu.add_radiobutton(label="ssh", variable=tipoConex, command=f_cambiarop, value=1)
    opciones_menu.add_radiobutton(label="sftp", variable=tipoConex, command=f_cambiarop, value=2)
    opciones_menu.add_radiobutton(label="rdp", variable=tipoConex, command=f_cambiarop, value=3)
    
    opciones_menu.add_separator()
    
    global tipoEmu
    tipoEmu=IntVar()
    tipoEmu.set(1) # y .get() para coger el valor
    opciones_menu.add_radiobutton(label="xterm",variable=tipoEmu, command=f_cambiarop, value=1)
    opciones_menu.add_radiobutton(label="uxterm",variable=tipoEmu, command=f_cambiarop, value=2)
    opciones_menu.add_radiobutton(label="xfc4-terminal",variable=tipoEmu, command=f_cambiarop, value=3)
    
    opciones_menu.add_separator()
    
    global tipoExp
    tipoExp=IntVar(value=1)
    opciones_menu.add_radiobutton(label="Thunar",variable=tipoEmu, command=f_cambiarop, value=1)
    opciones_menu.add_radiobutton(label="Nautilus",variable=tipoEmu, command=f_cambiarop, value=2)
    
    opciones_menu.add_separator()
    
    opciones_menu.add_command(label="Guardar",
                              accelerator="Crtl+g", underline=0,
                              state="disabled",  # DESABILITA ESTE SUBMENU MIENTRAS NO HAYA CAMBIOS QUE GUARDAR
                              command=f_guardar)
    
    #--------------------------------------- Ayuda (tercer Submenu)----------------------------------------
    ayuda_menu.add_command(label="Web", command=f_web) # LLama al metodo para abrir la pagina web
    ayuda_menu.add_command(label="Atajos de teclado")
    icon_acerca=PhotoImage(file=iconos_app[3])
    ayuda_menu.add_command(label="Acerca de",
                           image=icon_acerca, compound=LEFT,
                           command=f_acerca)
    
    # DEFINIR MENU CONTEXTUAL
    global menucontext
    menucontext = Menu(raiz.tk, tearoff=0)
    menucontext.add_command(label="Conectar", command=f_conectar)
    menucontext.add_command(label="Salir", command=quit)
    # Definimos un menu contextual pero no lo posicionamos esperamos a que surja el evento
    # para ponerlo con pos menucontext.post(x,y)
    
#     ------------------------------------- BARRA DE HERRAMIENTAS--------------------------------------------
    
    barraHerr=Box(raiz, width='fill', border=1)
    barraHerr.bg="#E5E5E5"
    barraHerr.tk.relief=RAISED # se supone que es un box elevado pero no lo veo claro.
    
    
    ic_bconectar = PhotoImage(file=iconos_app[4])
    b_conectar = PushButton(barraHerr, align='left', image=ic_bconectar, command=f_conectar)
    b_conectar.tk.pack(padx=1,pady=1)
    ic_bsalir = PhotoImage(file=iconos_app[5])
    b_salir = PushButton(barraHerr, text="salir", align='left', image=ic_bsalir, command=quit)
    b_salir.tk.pack(padx=1, pady=1)
#     COMPOUND. Especifica si el widget debe mostrar texto y mapas/imágenes al mismo tiempo, y si es así,
#     donde el mapa de bits o imagen debe estar en relación con el texto. Debe ser uno de los valores:
#     “none”, “bottom”, “top”, “left”, “right”, o “center” Por defecto esta en none.
# los .tk.pack(padx,pady) se refieren a pad externos al widget y los .tk.pack(ipadx,ipady a los internos)
    
    
# ---------------------------------------- BARRA DE ESTADO QUE ESTA ABAJO DL TODO--------------------------
    informacion = " "+platform.system()+" "+platform.node()+ " "+platform.machine()
    # Linux Ubuntu x86x64
    global b_estado
    b_estado=Box(raiz, align='bottom', border=1, width='fill')
    Text(b_estado, text=informacion, align='left')
        
 
#---------------------------  DEFINIMOS EL FUNCIONAMIENTO DE LAS TECLAS DE ACCESO RAPIDO -------------------
    def tecla_pulsada(evento):
        tecla= ord(evento.key) # ord nos devuelve el numero de tecla pulsada como un numero (unicode)
        print(tecla)
        if tecla==17: # 17 = valor en unicode de ctrl+q
            raiz.destroy()
        if tecla==3:
            f_conectar()
    '''En guizero los eventos se controlan mediante un gestor de eventos, que llaman a una funcion.
    Si a esa funcion le ponemos que use un parametro, este recibe datos del evento que le llama.
    Esto lo utilizaremos para las teclas de acceso rapido.'''
    
    raiz.when_key_pressed = tecla_pulsada
    raiz.when_right_button_pressed=menu_contextual
    
    raiz.display()

# ----------------------------METODOS PARA LOS MENUS DE LA BARRA DE MENUS--------------------
# Sesiones_menu():
def f_conectar():
    print("conectando...")
#---------------------------------------------    
def Opciones_menu():
    print("Opciones menu")
 
def barraEstado():
    if estado.get()==0:
        print(estado.get())
        b_estado.hide()
    else:
        print(estado.get())
        b_estado.show()
        
def f_cambiarop():
    ''' Habilitar opción 'Guardar' al elegir alguna opción
    de tipo de conexión, emulador de terminar o 
    explorador de archivos '''  
    opciones_menu.entryconfig("Guardar", state="normal") # config permite modificar una caracteristica ya
    #definida antes del objeto.

def f_guardar():
    '''guarda cuando haya cambios y vuelve a bloquearse hasta que vuelva a cambiar'''
    print("guardando configuracion")
    opciones_menu.entryconfig("Guardar", state="disabled") # En vez de por la etiqueta "Guardar" se puede poener
    # el numero del elemento en el menu. El 13 en nuestro caso.
    # el metodo entrycget nos da el valor que tiene un atributo en el menu en funcion de su posicion
    # en nuestro caso Guardar es el elemento 13 del submenu
    #if self.menu2.entrycget(13,"state")
    
# -------------------------------------------
def Ayuda_menu():
    print("Ayuda menu")

def f_web():
    ''' Abrir página web en navegador Internet al selecionar ayuda -> web'''
    
    pag1 = 'https://python-para-impacientes.blogspot.com/2016/03/menus-barras-de-herramientas-y-de.html'
    webbrowser.open_new_tab(pag1) # Abre la ventana que le hemos dicho en el navegador por defecto
    # del sistema.

def f_acerca():
    ''' Definir ventana de diálogo 'Acerca de' '''
    raiz.info("Acerca de...", text=__title__+" "+__version__+"\nprimera aplicacion en Guizero")
    # Equivale a messagebox de tkinter
    
#     Se podria haber hecho lanzando otra ventana pero he optado por guizero info para ahorrar codigo.
#     v_acerca = Window(raiz, title="Acerca de",width=320,height=230)
#     v_acerca.tk.resizable(width=False, height=False)
#     marco1=PushButton(v_acerca, image=iconos_app[4], enabled=False)
#     marco1.tk.place(relx=0.40,rely=0.07) # Posicionamiento relativo de [0-1] con respecto a la ventana padre.
    
def menu_contextual(valor):
    print('menu contextual')
    menucontext.post(valor.display_x, valor.display_y)



# ------------------------------------------ OTROS METODOS DEL PROGRAMA----------------------------------

def f_verifica_iconos(iconos): # Verifica que todos los iconos existen y estan en su sitio
    # el subdirectorio imagen
    for icono in iconos:
        if not os.path.exists(icono): # Comprueba que el icono en la ruta que le pasamos existe.
            print("Icono no Encontrado:", icono)
            return 1
    return 0       

    
# Inicializamos los iconos son sus rutas en el ordenador
img_carpeta=os.getcwd() # directorio de trabajo actual
img_carpeta=img_carpeta+os.sep+"imagen"+os.sep
# Al directorio de trabajo+os.sep (es el separador de directorios en el sistema en linux /)
# Al final direc_img es la ruta de los iconos en el subdirectorio imagen.
iconos_app=(img_carpeta + "pyremoto64x64.png",
            img_carpeta + "conec16x16.png",
            img_carpeta + "salir16x16.png",
            img_carpeta + "star16x16.png",
            img_carpeta + "conec32x32.png",
            img_carpeta + "salir32x32.png")
error1= f_verifica_iconos(iconos_app) # A la funcion verifica iconos le pasamos por parametro
# la lista de las rutas de todos los iconos de la aplicacion.
# La variable error1 sera 1 (True) si hay error y 0 (False) si no lo hay.

if not error1:
    Pyremote() 
    
