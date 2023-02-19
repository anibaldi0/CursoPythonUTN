import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Nombre: Anibal Caeiro

Al presionar el botón Mostrar pedir valores por prompt hasta que el usuario ingrese el valor 9 (se deberá utilizar 'BREAK').
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")

        self.valor_ingresado_int = 0
    def btn_mostrar_on_click(self):
        while(True):
            self.valor_ingresado_txt = prompt(title="", prompt="Ingrese un valor")
            if(self.valor_ingresado_txt == "9"):
                print("Cancelo con el 9")
                break
            else:
                self.valor_ingresado_int = int(self.valor_ingresado_txt)

        
    
if __name__ == "__main__":
    app = App()
    app.mainloop()