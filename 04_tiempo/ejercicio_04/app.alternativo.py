import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
from datetime import time
import customtkinter


'''
Nombre: Anibal
Apellido: Caeiro

Al presionar el botón INICIAR se debe mostrar un mensaje de bienvenida "Bienvenidos a la UTN FRA" cada 2 segundos, 
al mostrar el mensaje 5 veces que se detenga AUTOMÁTICAMENTE.

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
    '''
    Al presionar el botón INICIAR se debe mostrar un mensaje de bienvenida "Bienvenidos a la UTN FRA" cada 2 segundos, 
    al mostrar el mensaje 5 veces que se detenga AUTOMÁTICAMENTE.
    '''

    def btn_mostrar_on_click(self):
        self.resetear()
        self.mostrar_alert()

    def mostrar_alert(self):
        self.contador_mensajes_bienvenida += 1
        print(self.contador_mensajes_bienvenida)
        self.mostrar_mensaje_bienvenida = self.after(2000, self.mostrar_alert)
        alert(title="", message="Bienvenidos a la UTN FRA\nMensaje mostrado {0} veces".format(self.contador_mensajes_bienvenida))
        if(self.contador_mensajes_bienvenida > 4):
            self.after_cancel(self.mostrar_mensaje_bienvenida)
            alert(title="", message="Mensaje de Bienvenida Cancelado Automaticamente\ndespues de haberse mostrado {0} veces".format(self.contador_mensajes_bienvenida))
        
    def btn_cancelar_on_click(self):
        self.after_cancel(self.mostrar_mensaje_bienvenida)

    def resetear(self):
        self.contador_mensajes_bienvenida = 0

if __name__ == "__main__":
    app = App()
    app.mainloop()