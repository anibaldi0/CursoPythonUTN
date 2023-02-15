import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Anibal
apellido: Caeiro
---
Enunciado:
Al presionar el botón  'Mostrar', se deberá obtener contenido en la caja de texto y luego mostrarlo utilizando el Dialog Alert
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.label1 = customtkinter.CTkLabel(master=self, text="Nombre")
        self.label1.grid(row=0, column=0, padx=20, pady=10)
        
        self.txt_nombre = customtkinter.CTkEntry(master=self)
        self.txt_nombre.grid(row=0, column=1)
        
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        valor = self.txt_nombre.get() 
        alert(title='Alert', message = 'Hola ' + valor)

    '''
                    variables concatenadas ninja
    nombre = 'Pepe'
    apellido = 'Perez'
    sector = 'IT'
    saludo = 'Hola {0} {1}, trabajas en {2}'.format(nombre, apellido, sector)
    alert(title = 'Alerta', message = saludo)
    '''
    
if __name__ == "__main__":
    app = App()
    app.mainloop()