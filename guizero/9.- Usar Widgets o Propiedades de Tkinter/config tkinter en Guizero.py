from guizero import App, TextBox
app = App(width=300, height=200)
name = TextBox(app, text="Laura")
name.tk.config(cursor="target") 
app.display()