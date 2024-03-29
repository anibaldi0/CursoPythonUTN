import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Nombre: Anibal Caeiro

Al presionar el botón Mostrar pedir un número. mostrar los números divisores desde el 1 al número ingresado, 
y mostrar la cantidad de números divisores encontrados.
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
        self.numero_ingresado_txt = prompt(title="", prompt="Ingrese un numero")
        if(self.numero_ingresado_txt == None):
            print("Apreto Cancelar")
        else:
            self.numero_ingresado_int = int(self.numero_ingresado_txt)
            print(self.numero_ingresado_int)
            for numero in range(1, self.numero_ingresado_int + 1):
                if self.numero_ingresado_int % numero == 0:
                    self.contador_numeros_divisores += 1
                    self.lista_numeros_divisores = numero
                    print("El " + str(numero) + " es divisor de " + str(self.numero_ingresado_int))
            print("Hay " + str(self.contador_numeros_divisores) + " divisores encontrados")



    def resetear(self):
        self.numero_ingresado_int = None
        self.numero_ingresado_txt = None
        self.lista_numeros_divisores = []
        self.contador_numeros_divisores = 0

        
    
if __name__ == "__main__":
    app = App()
    app.mainloop()