import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import time
import customtkinter


'''
Nombre: Anibal
Apellido: Caeiro

Luego de presionar el botón 'Iniciar',se disparara un temporizador de una función que haga visible los tres botones ocultos. 
Se deberá calcular e informar la cantidad de segundos transcurridos desde que estos botones se hicieron visibles hasta el momento 
que el usuario logró pulsar todos los botones.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=1, pady=10, columnspan=2, sticky="nsew")

        self.btn_oculto_1 = customtkinter.CTkButton(master=self, text="Boton Oculto 1", command=self.btn_oculto_1_on_click)
        self.btn_oculto_2 = customtkinter.CTkButton(master=self, text="Boton Oculto 2", command=self.btn_oculto_2_on_click)
        self.btn_oculto_3 = customtkinter.CTkButton(master=self, text="Boton Oculto 3", command=self.btn_oculto_3_on_click)
        
        self.btn_oculto_4 = customtkinter.CTkButton(master=self, text="Check", command=self.btn_oculto_4_on_click)
        self.btn_oculto_4.grid(row=5, pady=10, columnspan=2, sticky="nsew")
        
        self.flag_btn_1 = False
        self.flag_btn_2 = False
        self.flag_btn_3 = False

        self.tiempo_inicial = 0

    def btn_mostrar_on_click(self):
        self.activar_boton_oculto()
        
    
    def btn_oculto_1_on_click(self):
        ts_fin_tempo_btn1 = time.time()
        self.ts_temporizador1 = ts_fin_tempo_btn1 - self.ts_inicio_temporizador
        #alert(title="", message="{} segundos".format(self.ts_temporizador1))
        self.flag_btn_1 = True

    def btn_oculto_2_on_click(self):
        ts_fin_tempo_btn2 = time.time()
        self.ts_temporizador2 = ts_fin_tempo_btn2 - self.ts_inicio_temporizador
        self.flag_btn_2 = True

    def btn_oculto_3_on_click(self):
        ts_fin_tempo_btn3 = time.time()
        self.ts_temporizador3 = ts_fin_tempo_btn3 - self.ts_inicio_temporizador
        self.flag_btn_3 = True
    
    #def 
    def btn_oculto_4_on_click(self):
        if(self.flag_btn_1 == True and self.flag_btn_2 == True and self.flag_btn_3 == True):
            self.ts_tempo_total = int(self.ts_temporizador1 + self.ts_temporizador2 + self.ts_temporizador3)
            alert(title="", message="El tiempo en apretar los 3 botones ocultos fue de: {0} segundos".format(self.ts_tempo_total))
            
    def activar_boton_oculto(self):
        self.btn_oculto_1.grid(row=2, pady=10, columnspan=2, sticky="nsew")
        self.btn_oculto_2.grid(row=3, pady=10, columnspan=2, sticky="nsew")
        self.btn_oculto_3.grid(row=4, pady=10, columnspan=2, sticky="nsew")
        
        self.ts_inicio_temporizador = time.time()
        

if __name__ == "__main__":
    app = App()
    app.mainloop()