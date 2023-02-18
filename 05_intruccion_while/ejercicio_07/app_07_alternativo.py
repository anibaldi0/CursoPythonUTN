import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario quiera, 
hasta que presione el botón Cancelar (en el prompt). 
Calcular la suma acumulada y el promedio de los números ingresados. 
Luego informar los resultados en las cajas de texto txt_suma_acumulada y txt_promedio

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")
        
        self.txt_suma_acumulada = customtkinter.CTkEntry(master=self, placeholder_text="Suma acumulada")
        self.txt_suma_acumulada.grid(row=0, padx=20, pady=20)

        self.txt_promedio = customtkinter.CTkEntry(master=self, placeholder_text="Promedio")
        self.txt_promedio.grid(row=1, padx=20, pady=20)

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")

        self.reset()

    def btn_comenzar_ingreso_on_click(self):
        self.reset()

        while (self.flag_inicio == True):
            self.numero_txt = prompt(title="", prompt="Ingrese un numero")
            self.numero_int = int(self.numero_txt)
            if(self.numero_txt != None):
                self.suma = self.suma + self.numero_int
                self.contador = self.contador + 1
                self.promedio = self.suma / self.contador
                print(self.suma)
                print(self.contador)
                print(self.promedio)

            else:
                break
            
            self.txt_suma_acumulada.delete(0, 1000)
            self.txt_suma_acumulada.insert(0, self.suma)
            
            self.txt_promedio.delete(0, 1000)
            self.txt_promedio.insert(0, self.promedio)
            
            
            

        print(self.suma)
        print(self.contador)
        print(self.promedio)
    
    def reset (self):
        self.suma = 0
        self.numero_int = 0
        self.contador = 0
        self.flag_inicio = True


    
if __name__ == "__main__":
    app = App()
    app.mainloop()
