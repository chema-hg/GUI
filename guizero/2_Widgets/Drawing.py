from guizero import App, Drawing
app = App(width=200, height=150)
drawing = Drawing(app)
drawing.rectangle(10, 10, 60, 60, color="blue")
app.display()
