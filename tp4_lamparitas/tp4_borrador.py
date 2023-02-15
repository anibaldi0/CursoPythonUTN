import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Nombre: Anibal
Apellido: Caeiro

Todas las lámparas están  al mismo precio de $800 pesos final.
		A.	Si compra 6 o más  lamparitas bajo consumo tiene un descuento del 50%. 
        
		B.	Si compra 5  lamparitas bajo consumo marca "ArgentinaLuz" se hace un descuento del 40 % 
            y si es de otra marca el descuento es del 30%.

		C.	Si compra 4  lamparitas bajo consumo marca "ArgentinaLuz" o “FelipeLamparas” se hace un descuento del 25 % 
            y si es de otra marca el descuento es del 20%.

		D.	Si compra 3  lamparitas bajo consumo marca "ArgentinaLuz"  el descuento es del 15%, si es  “FelipeLamparas” 
            se hace un descuento del 10 % y si es de otra marca un 5%.

		E.	Si el importe final con descuento suma más de $4000  se obtien un descuento adicional de 5%.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__() 

        # configure window
        self.title("UTN Fra")

        self.label1 = customtkinter.CTkLabel(master=self, text="Marca")
        self.label1.grid(row=0, column=0, padx=10, pady=10)
        
        self.combobox_marca = customtkinter.CTkComboBox(master=self, values=["ArgentinaLuz", "FelipeLamparas","JeLuz","HazIluminacion","Osram"])
        self.combobox_marca.grid(row=0, column=1, padx=10, pady=10)

        self.label2 = customtkinter.CTkLabel(master=self, text="Cantidad")
        self.label2.grid(row=1, column=0, padx=10, pady=10)

        self.combobox_cantidad = customtkinter.CTkComboBox(master=self, values= ["1", "2","3","4","5","6","7","8","9","10","11","12"])
        self.combobox_cantidad.grid(row=1, column=1, padx=10, pady=10)
                
        self.btn_calcular = customtkinter.CTkButton(master=self, text="Calcular", command=self.btn_calcular_on_click)
        self.btn_calcular.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_calcular_on_click(self):
        
        marca = self.combobox_marca.get()
        cantidad_txt = self.combobox_cantidad.get()
        cantidad_numero = int(cantidad_txt)
        precio = 800
        descuento = 0
        importe = precio * cantidad_numero
        importe_a_descontar = importe * descuento
        sub_total = importe * descuento
        
        
        mensaje = "Cantidad de lamparas: {0}\nMarca: {1}\nImporte a pagar: {2}\nEl descuento es de: {3}".format(cantidad_numero, marca, importe, importe_a_descontar)
        alert(title="", message=mensaje)
# A.	Si compra 6 o más  lamparitas bajo consumo tiene un descuento del 50%.
        if(cantidad_numero >= 6):
            descuento = 50/100
            alert(title="", message=mensaje + " CASO A 50%")
# B.	Si compra 5  lamparitas bajo consumo marca "ArgentinaLuz" se hace un descuento del 40 % y si es de otra marca el descuento es del 30%.
        elif(cantidad_numero == 5):
            if(marca == "ArgentinaLuz"):
                descuento = 40/100
                alert(title="", message=mensaje + " CASO B 40%")
            else:
                descuento = 30/100
                alert(title="", message=mensaje + " CASO B 30%")
# C.	Si compra 4  lamparitas bajo consumo marca "ArgentinaLuz" o “FelipeLamparas” se hace un descuento del 25 % y si es de otra marca el descuento es del 20%.
        elif(cantidad_numero == 4):
            if(marca == "ArgentinaLuz" or marca == "FelipeLamparas"):
                descuento = 25/100
                alert(title="", message=mensaje + " CASO C 25%")
            else:
                descuento = 20/100
                alert(title="", message=mensaje + " CASO C 20%")
# D.	Si compra 3  lamparitas bajo consumo marca "ArgentinaLuz"  el descuento es del 15%, si es  “FelipeLamparas” se hace un descuento del 10 % y si es de otra marca un 5%.
        elif(cantidad_numero == 3):
            if(marca == "ArgentinaLuz"):
                descuento = 15/100
                alert(title="", message=mensaje + " CASO D 15%")
            elif(marca == "FelipeLamparas"):
                descuento = 10/100
                alert(title="", message=mensaje + " CASO D 10%")
            else:
                descuento = 5/100
                alert(title="", message=mensaje + " CASO D 5%")
# E.	Si el importe final con descuento suma más de $4000  se obtien un descuento adicional de 5%.
        elif(sub_total > 4000):
            descuento = 5/100
            alert(title="", message=mensaje + " CASO E 5%")

        

        

if __name__ == "__main__":
    app = App()
    app.mainloop()