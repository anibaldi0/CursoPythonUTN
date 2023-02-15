import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


'''
Nombre: Anibal
Apellido: Caeiro

Una agencia de viajes cobra $15.000 por cada estadía como base. 
Luego para calcular las tarifas total realiza el siguiente cálculo, 
en función de la estación del año y del destino elegido:
    Si es invierno: 
        Bariloche tiene un aumento del 20% 
        Cataratas y Córdoba tienen un descuento del 10%
        Mar del plata tiene un descuento del 20%
    Si es Verano:
        Bariloche tiene un descuento del 20%
        Cataratas y Cordoba tienen un aumento del 10%
        Mar del plata tiene un aumento del 20%
    Si es Primavera u Otoño:
        Bariloche tiene un aumento del 10%
        Cataratas tiene un aumento del 10%
        Mar del plata tiene un aumento del 10%
        Córdoba tiene precio sin descuento

'''


class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        
        self.label_estaciones = customtkinter.CTkLabel(master=self, text="Estaciones")
        self.label_estaciones.grid(row=0, column=0, padx=20, pady=10)
        estaciones = ['Verano', 'Otoño', 'Invierno', 'Primavera']
        self.combobox_estaciones = customtkinter.CTkComboBox(master=self, values=estaciones)
        self.combobox_estaciones.grid(row=1, column=0, padx=20, pady=(10, 10))

        
        self.label_destinos = customtkinter.CTkLabel(master=self, text="Destinos")
        self.label_destinos.grid(row=2, column=0, padx=20, pady=10)
        destinos = ['Bariloche', 'Mar del plata', 'Cataratas', 'Cordoba']
        self.combobox_destino = customtkinter.CTkComboBox(master=self, values=destinos)
        self.combobox_destino.grid(row=3, column=0, padx=20, pady=(10, 10))

        
        self.btn_informar = customtkinter.CTkButton(master=self, text="Informar", command=self.btn_informar_on_click)
        self.btn_informar.grid(row=4, pady=20, columnspan=2, sticky="nsew")
        
    
    def btn_informar_on_click(self):
        destino = self.combobox_destino.get()
        estaciones = self.combobox_estaciones.get()
        descuento = 0
        estadia = 15000
        total = 0

        match (estaciones):
            case 'Verano':
                if(destino == 'Bariloche'):
                    descuento = 0.8
                elif(destino == 'Cataratas' and destino == 'Cordoba'):
                    descuento = 0.9
                else:
                    descuento = 0.9
            case 'Invierno':
                if(destino == 'Bariloche'):
                    descuento = 1.20
                elif(destino == 'Cataratas' or destino == 'Cordoba'):
                    descuento = 0.9
                elif(destino == 'Mar del plata'):
                    descuento = 0.8
            case _ :
                if(destino !='Cordoba'):
                    descuento = 1.1

        mensaje1 = "El costo de la estadia, con el descuento de {0} incluido es de: {1}".format(descuento, total)
        mensaje2 = "El costo de la estadia, con el aumento de {0} incluido es de: {1}".format(descuento, total)
        mensaje3 = "El costo de la estadia es de: {0}".format(total)

        total = estadia * descuento

        if(descuento < 1):
            mensaje = mensaje1
        elif(descuento > 1):
            mensaje = mensaje2
        elif(descuento == 0):
            mensaje = mensaje3

        alert(title="", message=mensaje)
        

            
    
if __name__ == "__main__":
    app = App()
    app.mainloop()