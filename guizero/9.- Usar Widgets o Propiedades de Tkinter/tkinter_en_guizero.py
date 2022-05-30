from guizero import App, TextBox, PushButton, Text

def show():
    output.value = textbox.value

app = App()
app.tk.geometry("300x200")
textbox = TextBox(app, multiline=True, height=5, width=50, scrollbar=True, text="a multiline\ntextbox")
textbox.tk['wrap'] = 'word' # Los valores pueden ser char, none or word
button = PushButton(app, text="Print", command=show)
output = Text(app)
app.display()