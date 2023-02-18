import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter
import random


'''
Nombre: Anibal Caeiro

Al presionar el botón Mostrar 5 veces un mensaje (utilizando el Dialog Alert) con números DESCENDENTES, desde el 5 al 1.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")

        self.lista_numeros = [5, 2, 1, 4, 3]
    def btn_mostrar_on_click(self):
        for numero in self.lista_numeros:
            self.lista_numeros.sort(reverse = True)
            alert(title="", message="Los numeros descendentes son {0}".format(numero))
        
            

if __name__ == "__main__":
    app = App()
    app.mainloop()