import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import time
import customtkinter
import random


'''
Nombre: Anibal Caeiro

En la pantalla se mostrarán 6 botones de distintos colores,  al comenzar el juego se mostrara el texto de un color entre los 6 posibles 
para que el jugador sepa que botón tocar .

Al tocar el botón correcto se informara cuanto tiempo tardo.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.btn_red = customtkinter.CTkButton(master=self, text="", command=lambda: self.btn_color_on_click("red"),fg_color="red")
        self.btn_red.grid(row=1, pady=10, columnspan=2, sticky="nsew")

        self.tiempo_inicial = time.time()

        self.btn_yellow = customtkinter.CTkButton(master=self, text="", command=lambda: self.btn_color_on_click("yellow"),fg_color="yellow")
        self.btn_yellow.grid(row=2, pady=10, columnspan=2, sticky="nsew")

        self.btn_pink = customtkinter.CTkButton(master=self, text="", command=lambda: self.btn_color_on_click("pink"),fg_color="pink")
        self.btn_pink.grid(row=3, pady=10, columnspan=2, sticky="nsew")

        self.btn_orange = customtkinter.CTkButton(master=self, text="", command=lambda: self.btn_color_on_click("orange"),fg_color="orange")
        self.btn_orange.grid(row=4, pady=10, columnspan=2, sticky="nsew")

        self.btn_blue = customtkinter.CTkButton(master=self, text="", command=lambda: self.btn_color_on_click("blue"),fg_color="blue")
        self.btn_blue.grid(row=5, pady=10, columnspan=2, sticky="nsew")

        self.btn_green = customtkinter.CTkButton(master=self, text="", command=lambda: self.btn_color_on_click("green"),fg_color="green",)
        self.btn_green.grid(row=6, pady=10, columnspan=2, sticky="nsew")
        
        self.color_seleccionado = None

        self.iniciar()
   
    def btn_color_on_click(self, color_elegido):
        pass
    
    def iniciar(self):
        pass

if __name__ == "__main__":
    app = App()
    app.mainloop()