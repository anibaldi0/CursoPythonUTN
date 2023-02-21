import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import time
import customtkinter
import random


'''
Nombre: Anibal Caeiro

El departamento de NUMEROS ESPECIALES  del instituto matemático  FonteCristo  nos está pidiendo una aplicación que verifique las distintas cualidades de los números.

Para cada una de estas acciones  debemos realizar la lógica para verificar las cualidades pedidas:
    A.	Se pedirán un número positivo y se mostrará la cantidad de números pares desde el número ingresado hasta el cero.
    B.	Se pedirán un número positivo y se mostrará la cantidad de números impares desde el número ingresado hasta el cero.
    C.	Se pedirán un número positivo y se mostrará la cantidad de números divisibles de este número que se encuentran desde el 1 al 100.
    D.	Se pedirán un número positivo y se mostrará si el número es un número primo o no.
    E.	Se pedirán un número positivo y se mostrará la cantidad de números Primos desde el número ingresado hasta el cero.

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.btn_A = customtkinter.CTkButton(master=self, text="A", command=lambda: self.btn_color_on_click("A"))
        self.btn_A.grid(row=1, pady=10, columnspan=2, sticky="nsew")

        self.btn_B = customtkinter.CTkButton(master=self, text="B", command=lambda: self.btn_color_on_click("B"))
        self.btn_B.grid(row=2, pady=10, columnspan=2, sticky="nsew")

        self.btn_C = customtkinter.CTkButton(master=self, text="C", command=lambda: self.btn_color_on_click("C"))
        self.btn_C.grid(row=3, pady=10, columnspan=2, sticky="nsew")

        self.btn_D = customtkinter.CTkButton(master=self, text="D", command=lambda: self.btn_color_on_click("D"))
        self.btn_D.grid(row=4, pady=10, columnspan=2, sticky="nsew")

        self.btn_E = customtkinter.CTkButton(master=self, text="E", command=lambda: self.btn_color_on_click("E"))
        self.btn_E.grid(row=5, pady=10, columnspan=2, sticky="nsew")
   
    def btn_color_on_click(self,valor):
        pass

if __name__ == "__main__":
    app = App()
    app.mainloop()