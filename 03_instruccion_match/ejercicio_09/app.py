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
        '''
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
        #la primera vez responde mal
        #tengo que preguntar dos veces el costo de la estadia para que me responda bien
        #por que podria ser este problema?
        self.estadia = 15000
        self.total = 0
        self.incremento = 0
        self.variacion = 0
        
    def btn_informar_on_click(self):
        self.estacion_del_ano = self.combobox_estaciones.get()
        print(self.estacion_del_ano)
        self.destino = self.combobox_destino.get()
        print(self.destino)
        match(self.estacion_del_ano):
            case 'Invierno':
                if(self.destino == 'Bariloche'):
                    self.incremento = 20
                elif(self.destino == 'Cataratas' or self.destino == 'Cordoba'):
                    self.incremento = -10
                elif(self.destino == 'Mar del plata'):
                    self.incremento = -20
            case 'Verano':
                if(self.destino == 'Bariloche'):
                    self.incremento = -20
                elif(self.destino == 'Cataratas' or self.destino == 'Cordoba'):
                    self.incremento = 10
                elif(self.destino == 'Mar del plata'):
                    self.incremento = 20
            case 'Otoño' | 'Primavera':
                if((self.destino == 'Bariloche' or self.destino == 'Cataratas') or self.destino == 'Mar del plata'):
                    self.incremento = 10
                else:
                    self.incremento = 0

        if(self.incremento >= 0):
            self.nombre_del_descuento = "Incremento"
        elif(self.incremento < 0):
            self.nombre_del_descuento = "Descuento"
        print(self.destino, self.nombre_del_descuento, self.incremento, self.estacion_del_ano, self.total)
        
        self.total = self.estadia + self.variacion
        self.variacion = self.estadia * (self.incremento / 100)
        mensaje = "El costo de la estadia en {0} es de 15000\nCon un {1} del {2} por se {3}\nEl costo total es {4}"
        mensaje = mensaje.format(self.destino, self.nombre_del_descuento, self.incremento, self.estacion_del_ano, self.total)
        alert(title="", message=mensaje)
    
if __name__ == "__main__":
    app = App()
    app.mainloop()