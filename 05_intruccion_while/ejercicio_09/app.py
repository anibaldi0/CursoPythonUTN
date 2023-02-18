import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Nombre: Anibal Caeiro

Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario quiera 
hasta que presione el botón Cancelar (en el prompt). 
Luego determinar el máximo y el mínimo 
e informarlos en los cuadros de textos txt_maximo y txt_minimo respectivamente

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")
        
        self.txt_minimo = customtkinter.CTkEntry(master=self, placeholder_text="Mínimo")
        self.txt_minimo.grid(row=0, padx=20, pady=20)

        self.txt_maximo = customtkinter.CTkEntry(master=self, placeholder_text="Máximo")
        self.txt_maximo.grid(row=1, padx=20, pady=20)

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")

        self.resetear()
    def btn_comenzar_ingreso_on_click(self):
        self.resetear()
        while (self.flag == True):
            self.numero_ingresado_txt = prompt(title="", prompt="Ingrese un numero")
            if(self.numero_ingresado_txt == None or self.numero_ingresado_txt == "0"):
                self.flag = False
                print("Sale porque preciono {0}".format(self.numero_ingresado_txt))
            else:
                self.numero_ingresado_int = int(self.numero_ingresado_txt)
                self.contador += 1
                if(self.maximo == None or self.numero_ingresado_int > self.maximo):
                    self.maximo = self.numero_ingresado_int

                if(self.minimo == None or self.numero_ingresado_int < self.minimo):
                    self.minimo = self.numero_ingresado_int
        
        self.txt_maximo.insert(0, self.maximo)
        self.txt_minimo.insert(0, self.minimo)

        mensaje = "El ultimo numero ingresado es {0}\nEl maximo es {1}\nEl minimo es {2}"
        mensaje = mensaje.format(self.numero_ingresado_int, self.maximo, self.minimo)
        print(mensaje)
                


    def resetear(self):
        self.txt_maximo.delete(0, 100)
        self.txt_minimo.delete(0, 100)
        self.maximo = None
        self.minimo = None
        self.contador = 0
        self.numero_ingresado_txt = None
        self.numero_ingresado_int = None
        self.flag = True

    
if __name__ == "__main__":
    app = App()
    app.mainloop()
