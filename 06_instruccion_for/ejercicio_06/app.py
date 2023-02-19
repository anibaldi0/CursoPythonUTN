import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Nombre: Anibal Caeiro

Al presionar el botón Mostrar pedir un número. mostrar los números pares desde 
el 1 al número ingresado, y mostrar la cantidad de números pares encontrados.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")

        self.resetear()
    def btn_mostrar_on_click(self):
        self.resetear()
        while(True):
            self.numero_ingresado_txt = prompt(title="", prompt="Ingrese un valor")
            if(self.numero_ingresado_txt != None):
                self.numero_ingresado_int = int(self.numero_ingresado_txt)
                self.lista_valores.append(self.numero_ingresado_int)
            else:
                break
            
        for valor in self.lista_valores:
            if(valor % 2 == 0):
                self.lista_pares.append(valor)
                self.contador_pares = len(self.lista_pares)
                
        print("Usted apreto Cancelar")
        mensaje = "Los numeros pares ingresados son {0}\nHa ingresado la cantidad de {1} numeros pares"
        mensaje = mensaje.format(self.lista_pares, self.contador_pares)
        alert(title="", message=mensaje)

    def resetear(self):
        self.lista_valores = []
        self.lista_pares = []
        self.contador_pares = 0
        
    
if __name__ == "__main__":
    app = App()
    app.mainloop()