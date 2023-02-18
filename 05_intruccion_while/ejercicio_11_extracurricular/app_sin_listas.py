import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Nombre: Anibal Caeiro

Enunciado:
Al presionarse el boton 'Comenzar ingreso', solicitar mediante prompt todos los numero que el usuario quiera, hasta que presione el boton Cancelar del prompt o ingrese cero.

Acumular los valores positivos y multiplicar entre si aquellos que son negativos (*informar por terminal)

Determinar el maximo, el minimo y el promedio de todos los numeros ingresados.
e informarlos en los cuadros de textos txt_maximo, txt_minimo y txt_promedio respectivamente

- resolver sin usar lista

'''

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()
        
        # configure windows
        self.title("UTN FRA")

        self.txt_minimo = customtkinter.CTkEntry(master=self, placeholder_text="Minimo")
        self.txt_minimo.grid(row=0, padx=20, pady=20)

        self.txt_maximo = customtkinter.CTkEntry(master=self, placeholder_text="Maximo")
        self.txt_maximo.grid(row=1, padx=20, pady=20)

        self.txt_promedio = customtkinter.CTkEntry(master=self, placeholder_text="Promedio")
        self.txt_promedio.grid(row=2, padx=20, pady=20)

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


        self.acumulador_positivos = 0
        self. acumulador_multiplos_negativos = None
        self.contador = 0
        self.maximo = None
        self.minimo = None

    def btn_comenzar_ingreso_on_click(self):
        self.flag_continuar = True
        while(self.flag_continuar == True):
            self.numero_ingresado_txt = prompt(title="", prompt="Ingrese un numero")
            print(self.numero_ingresado_txt)
            if(self.numero_ingresado_txt == None or self.numero_ingresado_txt == "0"):
                self.flag_continuar = False
            else:
                self.numero_ingresado_int = int(self.numero_ingresado_txt)
                self.contador = self.contador + 1

                if(self.maximo == None or self.numero_ingresado_int > self.maximo):
                    self.maximo = self.numero_ingresado_int

                if(self.minimo == None or self.numero_ingresado_int < self.minimo):
                    self.minimo = self.numero_ingresado_int

                if(self.numero_ingresado_int > 0):
                    self.acumulador_positivos = self.acumulador_positivos + self.numero_ingresado_int
                elif(self.numero_ingresado_int < 0):

                    if(self.acumulador_multiplos_negativos == None):
                        self.acumulador_multiplos_negativos = self.numero_ingresado_int
                    else:
                        self.acumulador_multiplos_negativos = self.acumulador_multiplos_negativos * self.numero_ingresado_int



            print("Suma de positivos " + str(self.acumulador_positivos))
            print("Multiplicacion de negativos " + str(self.acumulador_multiplos_negativos))
            print("Maximo " + str(self.maximo))
            print("Minimo " + str(self.minimo))
            print("Contador " + str(self.contador))


        print(self.numero_ingresado_txt)
        print("Saliste porque ingresaste '{0}'".format(self.numero_ingresado_txt))


if __name__ == "__main__":
    app = App()
    app.mainloop()