import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
from datetime import time
import customtkinter


'''
Nombre: Anibal
Apellido: Caeiro

Al presionar el botón INICIAR se debe mostrar un mensaje de bienvenida "Bienvenidos a la UTN FRA" cada 3 segundos. 
Al presionar el botón FINALIZAR se debe detener los mensajes.


'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=1, pady=10, columnspan=2, sticky="nsew")

        self.btn_cancelar = customtkinter.CTkButton(master=self, text="Cancelar", command=self.btn_cancelar_on_click)
        self.btn_cancelar.grid(row=2, pady=10, columnspan=2, sticky="nsew")

    def btn_mostrar_on_click(self):
        self.mostrar_alert()

    def mostrar_alert(self):
        alert(title="", message="Bienvenidos a la UTN FRA")
        self.mostrar_mensaje = self.after(3000, self.mostrar_alert)
        
    def btn_cancelar_on_click(self):
        self.after_cancel(self.mostrar_mensaje)

if __name__ == "__main__":
    app = App()
    app.mainloop()