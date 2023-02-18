import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Nombre: Anibal Caeiro

Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario 
quiera hasta que presione el botón Cancelar (en el prompt). 
Luego calcular:
    La suma acumulada de los negativos
    La suma acumulada de los positivos
    Cantidad de números positivos ingresados
    Cantidad de números negativos ingresados
    Cantidad de ceros
    Diferencia entre la cantidad de los números positivos ingresados y los negativos

Informar los resultados mediante alert()

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")
    
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")

        self.flag_comenzar = True
        self.numero_ingresado_int = None
        self.numero_ingresado_txt = None
        self.contador_general = 0
        self.contador_positivos = 0
        self.contador_negativos = 0
        self.contador_de_ceros = 0
        self.diferencia_positiv_menos_negativ = 0
        self.suma_positivos = 0
        self.suma_negativos = 0

        
    def btn_comenzar_ingreso_on_click(self):
        while(self.flag_comenzar == True):
            self.numero_ingresado_txt = prompt(title="", prompt="Ingrese un numero")
            if(self.numero_ingresado_txt == None):
                self.flag_comenzar = False
                print("Apreto Cancelar")
            else:
                self.numero_ingresado_int = int(self.numero_ingresado_txt)
                self.contador_general += 1
                if(self.numero_ingresado_int > 0):
                    self.contador_positivos += 1
                    self.suma_positivos = self.numero_ingresado_int + self.suma_positivos
                    print("suma de positivos " + str(self.suma_positivos))
                elif(self.numero_ingresado_int == 0):
                    self.contador_de_ceros += 1
                    print("Hay " + str(self.contador_de_ceros) + " ceros")
                elif(self.numero_ingresado_int < 0):
                    self.contador_negativos += 1
                    self.suma_negativos = self.suma_negativos + (self.numero_ingresado_int)
                    print("suma de negativos " + str(self.suma_negativos))
                self.diferencia_positiv_menos_negativ = self.contador_positivos - self.contador_negativos

        mensaje = "Ingreso {0} numros en total.\n{1} son positivos\n{2} son negativos\nIngreso {3} ceros\nLa suma de numeros positivos es {4}\nLa suma de numeros negativos es {5}\nLa diferencia de numeros positivos con los negativos es {6}"
        mensaje = mensaje.format(self.contador_general, self.contador_positivos, self.contador_negativos, self.contador_de_ceros, self.suma_positivos, self.suma_negativos, self.diferencia_positiv_menos_negativ)
        alert(title="", message=mensaje)

    
if __name__ == "__main__":
    app = App()
    app.mainloop()
