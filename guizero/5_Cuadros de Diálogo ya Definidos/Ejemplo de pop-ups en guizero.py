''' Ejemplos de ventanas emergentes '''
from guizero import *
from tkinter import colorchooser

raiz=App()

# Menu emergente para seleccionar un color
cp = colorchooser.askcolor()
print(cp)

warn('Ventana Warn', text='texto de ventana') #- popup box with a warning icon
info('Ventana Info', text='texto de la ventana') #- popup box with an information icon
error('Ventana Error', text='texto de la ventana') #- popup box with an error icon
yesno('Ventana Si/No', text='texto de la ventana') #- popup box with yes and no options. Pressing Yes returns True and pressing No returns False.
# Menu emergente para seleccionar un directorio. Pressing Yes returns True and
#pressing No returns False.
ask = question('Ventana de pregunta', 'texto ventana')
print(ask)
#- popup box with a question box which can accept a text response.
# Pressing Ok returns value entered into the box is returned
# and pressing Cancel returns None.

#Selecciona un directorio
directorio=select_folder(title="Select folder", folder=".")
print(directorio)

# Selecciona un archivo para cargar o guardar
select_file(title="Seleccionar un Archivo", folder=".",
            filetypes=[["All files", "*.*"]], save=False)
# popup file dialog box which asks the user to select a file.
# By default, an Open button is displayed,
#setting save to True will change the button to Save as.
#The path of the selected file is returned by the function.

#Usando un info como callback

button = PushButton(raiz, command=raiz.info, args=["Info", "Pulsaste un boton"], align='bottom')
'''Cuando pulsemos el boton, este ejecuta la llamada a la funcion inof y con args le pasamos
los argumentos que ha de tener esa como titulo y mensaje'''

raiz.display()