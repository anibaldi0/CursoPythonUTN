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

        nombre_lampara = self.combobox_marca.get()
        cantidad_txt = self.combobox_cantidad.get()
        cantidad_numero = int(cantidad_txt)
        precio = 800
        descuento = 0

        mensaje = "La marca es: {0} \n la cantidad es: {1}".format(nombre_lampara, cantidad_numero)
        #alert(title="", message=mensaje)

        if(cantidad_numero >= 6):
            descuento = 50/100
            alert(title="", message=mensaje + "\n CASO A")
        elif(cantidad_numero == 5):
            if(nombre_lampara == "ArgentinaLuz"):
                descuento = 40/100
                alert(title="", message=mensaje + "\n CASO B 40%")
            else:
                descuento = 30/100
                alert(title="", message=mensaje + "\n CASO B 30%")
        elif(cantidad_numero == 4):
            if(nombre_lampara == "ArgentinaLuz" or nombre_lampara == "FelipeLamparas"):
                descuento = 25/100
                alert(title="", message=mensaje + "\n CASO C 25%")
            else:
                descuento = 20/100
                alert(title="", message=mensaje + "\n CASO C 20%")
        elif(cantidad_numero == 3):
            if(nombre_lampara == "ArgentinaLuz"):
                descuento = 15/100
                alert(title="", message=mensaje + "\n CASO D 15%")
            elif(nombre_lampara == "FelipeLamparas"):
                descuento = 10/100
                alert(title="", message=mensaje + "\n CASO D 10%")
            else:
                descuento = 5/100
                alert(title="", message=mensaje + "\n CASO D 5%")
        elif(sub_total > 4000):
            alert(title="", message="Descuento extra")
        

        descuento_en_porcentaje = descuento * 100
        importe = cantidad_numero * precio

        ahorro = importe * descuento
        sub_total = importe - ahorro


        mensaje = "La cantidad es: {0}\nLa marca es: {1}\nEl importe es: {2}\nUd tiene un descuento del {3} %\nTotal a pagar es de: {4}\nSu ahorro es de: {5}".format(cantidad_numero, nombre_lampara, importe, descuento_en_porcentaje, sub_total, ahorro)
        alert(title="", message=mensaje)




if __name__ == "__main__":
    app = App()
    app.mainloop()