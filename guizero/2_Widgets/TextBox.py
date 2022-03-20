from guizero import App, TextBox, Box
raiz = App(width=200, height=150)

# no existen paddings para los box en guizero
# para lograr lo mismo hay que usar tkinter o como en
# este caso meter algo por medio.

# Caja de relleno que no se ve pero esta ahi
Box(raiz, align="top", width="fill", height=5)
# Caja Principal que contiene los inputs.
box = Box(raiz)

inputA = TextBox(box, width=20,text="Username")
inputB = TextBox(box, width=15, text="Password")
raiz.display()
