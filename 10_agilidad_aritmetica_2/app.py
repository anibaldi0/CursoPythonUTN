import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter
import random

'''
Nombre: Anibal Caeiro

Enunciado:
Debemos mostrar dos números Random del 1 al 10 y una de las operaciones básicas (suma, resta y multiplicación).
Solo debemos mostrar habilitado el boton de la operacion que salio seleccionada por el random, el resto de los botones se deberan 
mostrar deshabilitados 

En el cuadro de texto resultado el jugador debe ingresar el resultado de la operación y presionar el botón Aceptar.
Luego se debe informar si el resultado es el correcto o no.

Se agregara un temporizador que si no se responde luego de los 4(cuatro) segundos dará por terminado el juego.

Pista:
Para mostrar habilitado un boton podemos usar
self.nombre_boton.configure(state="enabled")

Para mostrar el boton inhabilitado un boton podemos usar:
self.nombre_boton.configure(state="disabled")

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.label1 = customtkinter.CTkLabel(master=self, text="Operador A")
        self.label1.grid(row=0, column=0, padx=20, pady=10)
        
        self.txt_operador_a = customtkinter.CTkEntry(master=self)
        self.txt_operador_a.grid(row=0, column=1)
        
        self.label2 = customtkinter.CTkLabel(master=self, text="Operador B")
        self.label2.grid(row=1, column=0, padx=20, pady=10)
        
        self.txt_operador_b = customtkinter.CTkEntry(master=self)
        self.txt_operador_b.grid(row=1, column=1)

        self.label3 = customtkinter.CTkLabel(master=self, text="Resultado")
        self.label3.grid(row=2, column=0, padx=20, pady=10)
        
        self.txt_respuesta = customtkinter.CTkEntry(master=self, fg_color="green")
        self.txt_respuesta.grid(row=2, column=1)
        
        self.btn_sumar = customtkinter.CTkButton(master=self, text="Sumar", command=self.btn_sumar_on_click)
        self.btn_sumar.grid(row=3, pady=10, columnspan=2, sticky="nsew")

        self.btn_restar = customtkinter.CTkButton(master=self, text="Restar", command=self.btn_restar_on_click)
        self.btn_restar.grid(row=4, pady=10, columnspan=2, sticky="nsew")

        self.btn_multiplicar = customtkinter.CTkButton(master=self, text="Multiplicar", command=self.btn_multiplicar_on_click)
        self.btn_multiplicar.grid(row=5, pady=10, columnspan=2, sticky="nsew")

        self.btn_jugar = customtkinter.CTkButton(master=self, text="JUGAR", command=self.btn_jugar_on_click, fg_color="green")
        self.btn_jugar.grid(row=6, pady=30, columnspan=2, rowspan=2,sticky="nsew")

    def deshabilitar_botones(self):
        pass
        
    def fin_por_respuesta(self):
        self.deshabilitar_botones()
        pass

    def btn_sumar_on_click(self):
        self.fin_por_respuesta()
        pass

    def btn_restar_on_click(self):
        self.fin_por_respuesta()
        pass
        
    def btn_multiplicar_on_click(self):
        self.fin_por_respuesta()
        pass
        
    def fin_por_tiempo(self):
        self.deshabilitar_botones()
        pass



    def btn_jugar_on_click(self):
        self.deshabilitar_botones()
        pass

if __name__ == "__main__":
    app = App()
    app.mainloop()