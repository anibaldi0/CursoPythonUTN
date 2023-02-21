import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Nombre: Anibal Caeiro

Al presionar el botón 'SUMA' se analizará el vector lista_datos a efectos de calcular 
el promedio el cual deberá ser informado utilizando Dialog Alert.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.btn_calcular = customtkinter.CTkButton(master=self, text="SUMATORIA", command=self.btn_calcular_on_click)
        self.btn_calcular.grid(row=2, pady=10, columnspan=2, sticky="nsew")

        self.lista_datos = [1,80,5,0,15,-5,1,79]

        self.suma_numeros = 0
        self.promedio = 0
    def btn_calcular_on_click(self):
        self.cantidad_numeros = len(self.lista_datos)
        for numero in self.lista_datos:
            self.suma_numeros = self.suma_numeros + numero
            print(self.suma_numeros)
            self.promedio = self.suma_numeros / self.cantidad_numeros
        print(self.promedio)
        alert(title="", message="La suma de los numeros de la lista es {0}".format(self.suma_numeros))
    
if __name__ == "__main__":
    app = App()
    app.mainloop()