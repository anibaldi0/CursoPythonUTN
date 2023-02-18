import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Nombre: Anibal Caeiro

Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar 5 números mediante prompt. 
Calcular la suma acumulada y el promedio de los números ingresados. 
Luego informar los resultados en las cajas de texto txt_suma_acumulada y txt_promedio

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")
        
        self.txt_suma_acumulada = customtkinter.CTkEntry(master=self, placeholder_text="Suma acumulada")
        self.txt_suma_acumulada.grid(row=0, padx=20, pady=20)

        self.txt_promedio = customtkinter.CTkEntry(master=self, placeholder_text="Promedio")
        self.txt_promedio.grid(row=1, padx=20, pady=20)

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")

        self.reset_inicio()

    def btn_comenzar_ingreso_on_click(self):
        self.reset_inicio()

        self.numero_txt = prompt(title="", prompt="Ingrese el primer numero de {0}".format(self.cantidad_numeros))
        self.numero_int += int(self.numero_txt)
        while(self.contador < 5):
            self.cantidad_numeros = self.cantidad_numeros - 1
            self.numero_txt = prompt(title="", prompt="Ingrese otro numero y faltan {0}".format(self.cantidad_numeros))
            self.numero_int += int(self.numero_txt)
            self.contador = self.contador + 1
            print(self.contador)
            print(self.numero_int)
        self.promedio = self.numero_int/self.contador
        self.txt_suma_acumulada.insert(0, self.numero_int)
        self.txt_promedio.insert(0, self.promedio)
        print("El promedio es " + str(self.promedio))
        print("La suma es " + str(self.numero_int))

    def reset_inicio(self):
        self.cantidad_numeros = 5
        self.numero_int = 0
        self.contador = 0
        self.txt_promedio.delete(0, 100)
        self.txt_suma_acumulada.delete(0, 100)
    
if __name__ == "__main__":
    app = App()
    app.mainloop()
