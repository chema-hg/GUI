from guizero import App, ListBox, Text
app = App(width=200, height=150)
Text(app, text="lista de la compra")
listbox = ListBox(app, items=["Pan", "Leche", "Carne", "Queso"])
app.display()
