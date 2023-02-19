import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Nombre: Anibal Caeiro

Al presionar el botón 'CARGAR' se le solicitarán tres números al usuario mediante el Dialog Prompt, los mismos deberán ser almacenados en un vector lista_datos. 
Al presionar el botón 'MOSTRAR', se deberán mostrar los números almacenados en el vector utilizando Dialog Alert para informar cada elemento.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=10, columnspan=2, sticky="nsew")

        self.btn_cargar = customtkinter.CTkButton(master=self, text="Cargar", command=self.btn_cargar_on_click)
        self.btn_cargar.grid(row=3, pady=10, columnspan=2, sticky="nsew")

        self.lista_datos = []

        self.resetear()
    def btn_mostrar_on_click(self):
        alert(title="", message="Los numeros de la lista son " + str(self.lista_datos))
        self.resetear()

    def btn_cargar_on_click(self):
        self.resetear()
        while(True):
            self.numero_ingresado_txt = prompt(title="", prompt="Ingrese un numero")
            if(self.numero_ingresado_txt == None):
                print("Usted apreto Cancelar")
                break
            else:
                self.numero_ingresado_int = int(self.numero_ingresado_txt)
                self.lista_datos.append(self.numero_ingresado_int)
                self.contar_numeros_lista = len(self.lista_datos)
                print(self.lista_datos)
                if(self.contar_numeros_lista == 3):
                    break

    def resetear(self):
        self.numero_ingresado_int = None
        self.numero_ingresado_txt = None
        self.lista_datos = []

        
        
if __name__ == "__main__":
    app = App()
    app.mainloop()