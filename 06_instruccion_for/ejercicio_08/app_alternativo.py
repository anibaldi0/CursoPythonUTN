import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Nombre: Anibal Caeiro

Al presionar el botón Mostrar pedir un número. Informar si el número es PRIMO o no.
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
        self.numero_ingresado_txt = prompt(title="", prompt="Ingrese un numero positivo")
        if(self.numero_ingresado_txt == None):
            print("Usted apreto Cancelar")
        else:
            self.numero_ingresado_int = int(self.numero_ingresado_txt)

            for numero in range(1, self.numero_ingresado_int + 1):
                if(self.numero_ingresado_int % numero == 0):
                    print(str(numero) + " es multiplo de " + str(self.numero_ingresado_int))
                    self.contador_divisores += 1
            print("tiene {0} divisores".format(self.contador_divisores))
        if(self.contador_divisores < 3):
            print("El numero {0} es primo".format(self.numero_ingresado_int))
            



    def resetear (self):
        self.numero_ingresado_int = None
        self.numero_ingresado_txt = None
        self.contador_divisores = 0
    
if __name__ == "__main__":
    app = App()
    app.mainloop()