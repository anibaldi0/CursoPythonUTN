import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Nombre:Anibal Caeiro

Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario quiera, 
hasta que presione el botón Cancelar (en el prompt) o el usuario ingrese cero. 
Calcular la suma acumulada de los positivos y multiplicar los negativos. 
Luego informar los resultados en las cajas de texto txt_suma_acumulada y txt_producto

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")
        
        self.txt_suma_acumulada = customtkinter.CTkEntry(master=self, placeholder_text="Suma acumulada")
        self.txt_suma_acumulada.grid(row=0, padx=20, pady=20)

        self.txt_producto = customtkinter.CTkEntry(master=self, placeholder_text="Producto")
        self.txt_producto.grid(row=1, padx=20, pady=20)

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")
        '''
        Enunciado:
        Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario quiera, 
        hasta que presione el botón Cancelar (en el prompt) o el usuario ingrese cero. 
        Calcular la suma acumulada de los positivos y multiplicar los negativos.
        Luego informar los resultados en las cajas de texto txt_suma_acumulada y txt_producto
        '''

        self.reinicio()

    def btn_comenzar_ingreso_on_click(self):
        self.reinicio()
        self.numero_ingresado_txt = prompt(title="", prompt="Ingrese un numero")
        self.numero_ingresado_int = int(self.numero_ingresado_txt)
        #print(self.numero_ingresado_int)

        while (self.numero_ingresado_int != None):
            self.numero_ingresado_int = int(self.numero_ingresado_txt)
            self.contador = self.contador + 1
            self.suma = self.suma + self.numero_ingresado_int
            if (self.numero_ingresado_int != 0):
                self.numero_ingresado_txt = prompt(title="", prompt="Ingrese otro numero")
                self.numero_ingresado_int = int(self.numero_ingresado_txt)
                #self.suma = self.suma + self.numero_ingresado_int
                self.contador = self.contador + 1
                print("num ingresado " + str(self.numero_ingresado_int))
                print("suma es " + str(self.suma))
            else:
                break
        
        self.txt_suma_acumulada.delete(0, 100)
        self.txt_suma_acumulada.insert(0, self.suma)

        #self.txt_producto.insert(0, )


    def reinicio(self):
        self.numero_ingresado_int = None
        self.contador = 0
        self.suma = 0


    
if __name__ == "__main__":
    app = App()
    app.mainloop()
