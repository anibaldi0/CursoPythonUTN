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
    '''
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
    
    def btn_calcular_on_click(self):
        self.reasetear()
        self.marca = self.combobox_marca.get()
        self.cantidad_lamparas_int = int(self.combobox_cantidad.get())
        
        if(self.cantidad_lamparas_int >= 6):
            self.descuento = 50
        if(self.marca != "ArgentinaLuz" and self.cantidad_lamparas_int == 5):
            self.descuento = 30
        if((self.marca != "ArgentinaLuz" or self.marca != "FelipeLamparas") and self.cantidad_lamparas_int == 4):
            self.descuento = 20

        match(self.marca):
            case "ArgentinaLuz":
                if(self.cantidad_lamparas_int == 5):
                    self.descuento = 40
                elif(self.cantidad_lamparas_int == 4):
                    self.descuento = 25
                elif(self.cantidad_lamparas_int == 3):
                    self.descuento = 15
            case "FelipeLamparas":
                if(self.cantidad_lamparas_int == 4):
                    self.descuento = 25
                elif(self.cantidad_lamparas_int == 3):
                    self.descuento = 10
            case _ :
                if(self.cantidad_lamparas_int == 3):
                    self.descuento = 5

        self.importe_sin_descuento = self.precio * self.cantidad_lamparas_int
        self.ahorro = self.importe_sin_descuento * (self.descuento/100)
        self.total_con_descuento = self.importe_sin_descuento - self.ahorro
        self.importe_con_ahorro_extra = self.total_con_descuento - self.ahorro_extra

        mensaje = "Importe sin descuento {0}\nDescuento del {1}\nTotal con descuento {2}\nAhorro {3}"
        mensaje = mensaje.format(self.importe_sin_descuento, self.descuento, self.total_con_descuento, self.ahorro)
        alert(title="", message=mensaje)
        if(self.total_con_descuento > 4000):
            self.ahorro_extra = self.total_con_descuento * 0.05
            mensaje = "Tiene un descuento extra por superar los 4000\nEl descuento es del 5% y se ahorra {0}\nPor lo que el precio final es de {1}".format(self.ahorro_extra, self.importe_con_ahorro_extra)
            alert(title="", message=mensaje)

    def reasetear(self):
        
        self.ahorro = 0
        self.ahorro_extra = 0
        self.descuento = 0
        self.precio = 800

if __name__ == "__main__":
    app = App()
    app.mainloop()