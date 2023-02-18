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
Al presionar el botón  'Mostrar', se deberá obtener un dato utilizando el Dialog Prompt
y luego mostrarlo utilizando el Dialog Alert
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")
    
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostar", command=self.btn_mostrar_on_click) # se declara un boton
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew") #se posiciona el boton


    def btn_mostrar_on_click(self):
    
        result = prompt(title='Prompt', prompt='Ingrese un valor')
        alert(title='Ingrese un valor', message='El valor ingresado es ' + result)

    # variante del ejercicio en clase
    #titulo = 'Pregunta'
    #nombre = prompt(title='Pregunta',prompt='Escriba su nombre')
    #mensaje = 'Hola ' + nombre + 'Como estas?'
    #alert(title='Info', message=mensaje)

    
        
        
    
if __name__ == "__main__":
    app = App()
    app.mainloop()