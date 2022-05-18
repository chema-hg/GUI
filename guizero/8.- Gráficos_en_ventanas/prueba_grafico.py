from guizero import *
'''Una forma de insertar un grafico es construyendolo con matplotlib,
guardandolo con la instrucion savefig()
y luego importarlo en guizero con Picture()'''

raiz=App()
Picture(raiz, image="grafico1.png", width=500, height=500)
raiz.display()