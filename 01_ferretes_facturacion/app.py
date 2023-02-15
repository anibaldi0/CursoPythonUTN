import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Enunciado:
Para el departamento de facturación:
    A.	Ingresar tres precios de productos y mostrar la suma de los mismos.
    B.	Ingresar tres precios de productos y mostrar el promedio de los mismos.
	C.	ingresar tres precios de productos sumarlos y mostrar precio final (más IVA 21%).
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.label_1 = customtkinter.CTkLabel(master=self, text="Producto 1")
        self.label_1.grid(row=0, column=0, padx=20, pady=10)
        
        self.txt_importe_1 = customtkinter.CTkEntry(master=self)
        self.txt_importe_1.grid(row=0, column=1)

        self.label_2 = customtkinter.CTkLabel(master=self, text="Producto 2")
        self.label_2.grid(row=1, column=0, padx=20, pady=10)
        
        self.txt_importe_2 = customtkinter.CTkEntry(master=self)
        self.txt_importe_2.grid(row=1, column=1)

        self.label_3 = customtkinter.CTkLabel(master=self, text="Producto 3")
        self.label_3.grid(row=2, column=0, padx=20, pady=10)
        
        self.txt_importe_3 = customtkinter.CTkEntry(master=self)
        self.txt_importe_3.grid(row=2, column=1)
       
        self.btn_total = customtkinter.CTkButton(master=self, text="TOTAL", command=self.btn_total_on_click)
        self.btn_total.grid(row=3, pady=10, columnspan=2, sticky="nsew")
        
        self.btn_promedio = customtkinter.CTkButton(master=self, text="PROMEDIO", command=self.btn_promedio_on_click)
        self.btn_promedio.grid(row=4, pady=10, columnspan=2, sticky="nsew")

        self.btn_total_iva = customtkinter.CTkButton(master=self, text="TOTAL c/IVA", command=self.btn_total_iva_on_click)
        self.btn_total_iva.grid(row=5, pady=10, columnspan=2, sticky="nsew")

    def btn_total_on_click(self):
        precio_texto1 = self.txt_importe_1.get()
        precio_numero1 = float(precio_texto1)

        precio_texto2 = self.txt_importe_2.get()
        precio_numero2 = float(precio_texto2)

        precio_texto3 = self.txt_importe_3.get()
        precio_numero3 = float(precio_texto3)

        suma = precio_numero1 +  precio_numero2 + precio_numero3

        alert(title="", message="La suma es: " + str(suma))

    def btn_promedio_on_click(self):
        precio_texto1 = self.txt_importe_1.get()
        precio_numero1 = float(precio_texto1)

        precio_texto2 = self.txt_importe_2.get()
        precio_numero2 = float(precio_texto2)

        precio_texto3 = self.txt_importe_3.get()
        precio_numero3 = float(precio_texto3)

        suma = precio_numero1 +  precio_numero2 + precio_numero3

        promedio = suma/3

        alert(title="", message="El promedio es: " + str(promedio))
        

    def btn_total_iva_on_click(self):
        precio_texto1 = self.txt_importe_1.get()
        precio_numero1 = float(precio_texto1)

        precio_texto2 = self.txt_importe_2.get()
        precio_numero2 = float(precio_texto2)

        precio_texto3 = self.txt_importe_3.get()
        precio_numero3 = float(precio_texto3)

        suma = precio_numero1 +  precio_numero2 + precio_numero3

        precio_mas_iva = suma * 1.21

        alert(title="", message="Importe mas IVA es: " + str(precio_mas_iva))

    
if __name__ == "__main__":
    app = App()
    app.mainloop()