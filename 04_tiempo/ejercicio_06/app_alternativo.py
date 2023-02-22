import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
from datetime import time
import customtkinter


'''
Nombre: Anibal
Apellido: Caeiro

Luego de presionar el botón 'Iniciar', se inhabilita el botón durante 3(tres) segundos
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=1, pady=10, columnspan=2, sticky="nsew") #con .grid_forget lo oculto


    def btn_mostrar_on_click(self):
        self.ocultar_boton()
        self.after(3000, self.mostrar_botones)

    def mostrar_botones(self):
        self.btn_mostrar.grid(row=1, pady=10, columnspan=2, sticky="nsew")

    def ocultar_boton(self):
        self.btn_mostrar.grid_forget()

if __name__ == "__main__":
    app = App()
    app.mainloop()