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
        '''
        Luego de presionar el botón 'Iniciar',se disparara un temporizador de una función que haga visible los tres botones ocultos. 
        Se deberá calcular e informar la cantidad de segundos transcurridos desde que estos botones se hicieron visibles hasta el momento 
        que el usuario logró pulsar todos los botones.
        '''

    def btn_mostrar_on_click(self):
        self.activar_boton_oculto()
        self.resetear()

    def btn_oculto_1_on_click(self):
        self.ts_fin_temporizador_boton_1 = time.time()
        self.ts_tiempo_transcurrido_1 = self.ts_fin_temporizador_boton_1 - self.ts_inicio_temporizador
    def btn_oculto_2_on_click(self):
        self.ts_fin_temporizador_boton_2 = time.time()
        self.ts_tiempo_transcurrido_2 = self.ts_fin_temporizador_boton_2 - self.ts_inicio_temporizador
    def btn_oculto_3_on_click(self):
        self.ts_fin_temporizador_boton_3 = time.time()
        self.ts_tiempo_transcurrido_3 = self.ts_fin_temporizador_boton_3 - self.ts_inicio_temporizador 
    def btn_oculto_4_on_click(self):
        self.fin_temporizadores()
        print(self.ts_tiempo_total_transcurrido)
        self.ocultar_botones()
        alert(title="", message="El tiempo transcurrido es de {0} segundos".format(int(self.ts_tiempo_total_transcurrido)))
        
    def fin_temporizadores(self):
        self.ts_tiempo_total_transcurrido = self.ts_tiempo_transcurrido_1 + self.ts_tiempo_transcurrido_2 + self.ts_tiempo_transcurrido_3

    def ocultar_botones(self):
        self.btn_oculto_1.grid_forget()    
        self.btn_oculto_2.grid_forget()        
        self.btn_oculto_3.grid_forget()
        self.btn_oculto_4.grid_forget()    
    def activar_boton_oculto(self):
        self.btn_oculto_1.grid(row=2, pady=10, columnspan=2, sticky="nsew")
        self.btn_oculto_2.grid(row=3, pady=10, columnspan=2, sticky="nsew")
        self.btn_oculto_3.grid(row=4, pady=10, columnspan=2, sticky="nsew")
        self.btn_oculto_4.grid(row=5, pady=10, columnspan=2, sticky="nsew")

    def resetear(self):
        self.ts_inicio_temporizador = time.time()

        

if __name__ == "__main__":
    app = App()
    app.mainloop()