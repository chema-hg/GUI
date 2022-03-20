'''Crea una ventana don dos botones uno da informacion de la ventana y otro para salir'''

from guizero import *

class Aplicacion():    
      
    def __init__(self):
        
        self.raiz=App(title='Ver Info', bg='beige', width=310, height=210)
        
        # Vamos a impedir que los bordes puedan desplazarse para
        # ampliar o reducir el tamaño de la ventana 'self.raiz'. Esto no esta disponible directamente en guizero.
        # En guizero no encontre la opcion para no poder cambiar el tamaño de la ventana, asi que
        # como al fin y al cabo la raiz es un objeto de tk uso una orden de tk.resizable()
        self.raiz.tk.resizable(width=False, height=False)
        
        self.tinfo = TextBox(self.raiz, width=40, height=10, multiline=True,text="")
        self.tinfo.bg='white'
        
        self.binfo = PushButton(self.raiz, text='Info', align='left', padx=25, pady=2, command=self.verinfo)
        self.binfo.focus()
        self.binfo.when_mouse_enters=self.claro
        
        
        self.bsalir = PushButton(self.raiz, text='Salir', align='right', padx=25, pady=2, command=self.raiz.destroy)
        self.bsalir.when_mouse_enters=self.claro
        
    def verinfo(self):
            
        info1 = self.raiz.tk.winfo_class()
        info2 = self.raiz.tk.winfo_geometry()
        info3 = str(self.raiz.tk.winfo_width())
        info4 = str(self.raiz.tk.winfo_height())
        info5 = str(self.raiz.tk.winfo_rootx())
        info6 = str(self.raiz.tk.winfo_rooty())
        info7 = str(self.raiz.tk.winfo_id())
        info8 = str(self.raiz.tk.winfo_name())
        info9 = str(self.raiz.tk.winfo_manager())
            
        texto_info = "Clase de 'raiz': " + info1 + "\n"
        texto_info += "Resolución y posición: " + info2 + "\n"
        texto_info += "Anchura ventana: " + info3 + "\n"
        texto_info += "Altura ventana: " + info4 + "\n"
        texto_info += "Pos. Ventana X: " + info5 + "\n"
        texto_info += "Pos. Ventana Y: " + info6 + "\n"
        texto_info += "Id. de 'raiz': " + info7 + "\n"
        texto_info += "Nombre objeto: " + info8 + "\n" 
        texto_info += "Gestor ventanas: " + info9 + "\n"
            
        print(texto_info)
        self.tinfo.value=texto_info
        
    def claro(self, event_data):
        event_data.widget.bg="#ececec"
        #evento para cuando el raton sale del boton que vuelva la color normal
        event_data.widget.when_mouse_leaves=self.normal
        
    def normal(self, event_data):
        event_data.widget.bg="#f5f5dc"
        
          
        
        
        
def main():
    mi_app = Aplicacion()
    return 0

if __name__ == '__main__':
    
    main()