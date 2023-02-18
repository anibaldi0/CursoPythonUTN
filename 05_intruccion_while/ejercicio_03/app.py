import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


'''
Nombre: Anibal Caeiro

Enunciado:
Al presionar el botón ‘Pedir clave’, solicitar al usuario que ingrese una contraseña mediante prompt. 
Comprobar que la contraseña ingresada sea ‘utn750’. En caso de no coincidir, volverla a solicitar hasta que coincidan
'''


class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        
        self.btn_pedir_clave = customtkinter.CTkButton(master=self, text="Ingresar", command=self.btn_pedir_clave_on_click)
        self.btn_pedir_clave.grid(row=2, pady=20, columnspan=2, sticky="nsew")
        
        self.clave = "utn750"
    def btn_pedir_clave_on_click(self):
        self.clave = prompt(title="", prompt="Introduzca su Clave")
        while (self.clave != "utn750"):
            self.clave = prompt(title="", prompt="Introduzca la Clave Correcta")
        alert(title="", message="Clave Correcta")
            
    
    
if __name__ == "__main__":
    app = App()
    app.mainloop()