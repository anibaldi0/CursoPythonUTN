import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''

Nombre: Anibal
Apellido: Caeiro

Enunciado:

2.	El departamento de Construcción Rural requiere una herramienta que facilite el calculo de materiales necesarios 
a la hora de realizar un alambrado permetral, se le solicita al usuario que ingrese el ancho y el largo del terreno.

    A. Informar los metros cuadrados del terreno y los metros lineales del perimetro
    B. Informar la cantidad de postes de quebracho Grueso de 2.4 mts (van cada 250 mts lineales y en las esquinas).
    C. Informar la cantidad de postes de quebracho Fino de 2.2 mts (van cada 12 mts lineales, si en es lugar no se encuentra el poste grueso).
    D. Informar la cantidad de varillas (van cada 2 mts lineales).
    E. Informar la cantidad de alambre alta resistencia 17/15 considerando 7 hilos.

    EJ 36 MTS X 24 MTS 
    (G)Poste Quebracho Grueso de 2.4 mts
    (V)Poste Quebracho Fino de 2.2 mts
    (F)Varillas
    
    G V V V V V F V V V V V F V V V V V G
    V                                   V
    V                                   V
    V                                   V
    V                                   V
    V                                   V
    F                                   F
    V                                   V
    V                                   V
    V                                   V
    V                                   V
    V                                   V
    G V V V V V F V V V V V F V V V V V G
    
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.label_1 = customtkinter.CTkLabel(master=self, text="Largo")
        self.label_1.grid(row=0, column=0, padx=20, pady=10)
        
        self.txt_largo = customtkinter.CTkEntry(master=self)
        self.txt_largo.grid(row=0, column=1)

        self.label_2 = customtkinter.CTkLabel(master=self, text="Ancho")
        self.label_2.grid(row=1, column=0, padx=20, pady=10)
        
        self.txt_ancho = customtkinter.CTkEntry(master=self)
        self.txt_ancho.grid(row=1, column=1)
       
        self.btn_calcular = customtkinter.CTkButton(master=self, text="CALCULAR", command=self.btn_calcular_on_click)
        self.btn_calcular.grid(row=3, pady=10, columnspan=2, sticky="nsew")
        

    def btn_calcular_on_click(self):
        largo_texto = self.txt_largo.get()
        largo_numero = int(largo_texto)

        ancho_texto = self.txt_ancho.get()
        ancho_numero = int(self.txt_ancho.get())

        perimetro = (largo_numero * 2 ) + (ancho_numero * 2)
        area = (largo_numero * ancho_numero)

        poste_grueso_largo = int((largo_numero - 1)/250)
        poste_grueso_largo_total = (poste_grueso_largo * 2) + 2
        poste_grueso_ancho = int((ancho_numero - 1)/250)
        poste_grueso_ancho_total = (poste_grueso_ancho * 2) + 2
        poste_grueso = int(poste_grueso_largo_total) + int(poste_grueso_ancho_total)

        poste_fino = (int(largo_numero / 12) * 2) + (int(ancho_numero / 12) * 2)

        varillas = (int(largo_numero / 2) * 2) + (int(ancho_numero / 2) * 2)

        alambre = (largo_numero * 2 + ancho_numero * 2) * 7

        medidas = """El perimetro del terreno es {0}mts
        El Area del terreno es {1}m2
        La cantidad de postes a usar son: {2}
        La cantidad de postes finos son: {3}
        La cantidad de varillas son: {4}
        La cantidad de alambre son {5}mts""".format(perimetro, area, poste_grueso, poste_fino, varillas, alambre)

        alert(title="", message=medidas)

    
    
if __name__ == "__main__":
    app = App()
    app.mainloop()