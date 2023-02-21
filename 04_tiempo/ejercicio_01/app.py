import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
from datetime import time
import customtkinter


'''
Nombre: Anibal
Apellido: Caeiro

Enunciado:
Al presionar el botón INICIAR se debe mostrar un mensaje de bienvenida "Bienvenidos a la UTN FRA" cada 3 segundos. 

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=1, pady=10, columnspan=2, sticky="nsew")

    def btn_mostrar_on_click(self):
        self.after(1000, self.mostrar_alert)

    def mostrar_alert (self):
        alert(title="", message="Bienvenidos a la UTN FRA")
        
        

if __name__ == "__main__":
    app = App()
    app.mainloop()