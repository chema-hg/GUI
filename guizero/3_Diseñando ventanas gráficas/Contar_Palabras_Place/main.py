# se puede usar como ejemplo la siguiente pagina
# https://www.gutenberg.org/cache/epub/2000/pg2000.txt

from guizero import *
import modquijote as qj

max_frec = 20  # numero maximo de palabras a mostrar en la tabla de frecuencias


def pasar_datos():
    print(url.value)
    texto = qj.descargar_pagina(url.value)
    t4.value = texto
    frec_items = qj.contar_palabras(texto)
    for k, v in frec_items[:max_frec]:
        show=f"{k:17} {v}"
        t5.append(show)


raiz = App(title='Contador de palabras en la red')
raiz.tk.geometry("700x400+350+150")
raiz.tk.resizable(0, 0)

t1 = Text(raiz, text='Direccion:', visible=False)
t1.tk.place(relx=.03, rely=0.05)
url = TextBox(raiz, width=50, text=" ", visible=False)
url.tk.place(relx=.15, rely=0.05)
but1 = PushButton(raiz, text='Descargar', visible=False,
                  pady=3, command=pasar_datos)
but1.tk.place(relx=0.75, rely=0.045)

t2 = Text(raiz, text='Texto: ', visible=False)
t2.tk.place(relx=.03, rely=0.15)
t3 = Text(raiz, text='Tabla de frecuencias:', visible=False)
t3.tk.place(relx=.65, rely=0.15)
t4 = TextBox(raiz, text='Prueba', height=15,
             width=50, multiline=True, visible=False, scrollbar=True)
t4.tk.place(relx=.03, rely=0.25)
t5 = TextBox(raiz, text='Palabra    |   Frecuencia', height=15,
             width=25, multiline=True, visible=False)
t5.tk.place(relx=.65, rely=0.25)
raiz.display()
