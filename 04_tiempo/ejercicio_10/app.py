import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import time
import customtkinter


'''
Nombre: Anibal
Apellido: Caeiro

Luego de presionar el botón 'Iniciar',se disparara ; un temporizador de una función que haga visible los tres botones ocultos. 
Se deberá calcular e informar la cantidad de segundos transcurridos desde que estos botones se hicieron visibles hasta el momento 
que el usuario logró pulsar todos los botones. 

Continuando con el ejercicio anterior, se deberán incorporar los siguientes mensajes. 
    *si tardo menos de 1 segundo :"Usted es Flash". 
    *si tardo entre 1 y 2 segundos :"Bien ahí". 
    *si tardo entre 2 y 3 segundos :"Medio lenteja". 
    *si tardo más de 3 segundos :"¿Te quedaste dormido?".
    
Luego de informar el tiempo reiniciar el juego.
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
        self.btn_check_all = customtkinter.CTkButton(master=self, text="Check all", command=self.btn_oculto_3_on_click)

    def btn_mostrar_on_click(self):
        self.resetear()
        self.activar_boton_oculto()
        
    def btn_oculto_1_on_click(self):
        self.ts_fin_temporizador_1 = time.time()
        self.tiempo_1 = self.ts_fin_temporizador_1 - self.ts_inicio_temporizador
        self.lista_tiempos.append(self.tiempo_1)
        #print(self.tiempo_1)

    def btn_oculto_2_on_click(self):
        self.ts_fin_temporizador_2 = time.time()
        self.tiempo_2 = self.ts_fin_temporizador_2 - self.ts_inicio_temporizador
        self.lista_tiempos.append(self.tiempo_2)
        #print(self.tiempo_2)

    def btn_oculto_3_on_click(self):
        self.ts_fin_temporizador_3 = time.time()
        self.tiempo_3 = self.ts_fin_temporizador_3 - self.ts_inicio_temporizador
        self.lista_tiempos.append(self.tiempo_3)
        #print(self.tiempo_3)

    def btn_check_all_press(self):
        for self.tiempo in self.lista_tiempos:
            if(self.tiempo_maximo == None or self.tiempo > self.tiempo_maximo):
                self.tiempo_maximo = self.tiempo
                print(self.tiempo_maximo)

    def fin_temporizador(self):
        self.ts_tiempo_final_total = self.tiempo_1 + self.tiempo_2 + self.tiempo_3
        print(self.ts_tiempo_final_total)

    def resetear(self):
        self.tiempo_maximo = None
        self.ts_inicio_temporizador = time.time()
        self.lista_tiempos = []
        self.tiempo = 0
        
    def activar_boton_oculto(self):
        self.btn_oculto_1.grid(row=2, pady=10, columnspan=2, sticky="nsew")    
        self.btn_oculto_2.grid(row=3, pady=10, columnspan=2, sticky="nsew")    
        self.btn_oculto_3.grid(row=4, pady=10, columnspan=2, sticky="nsew")
        self.btn_check_all.grid(row=5, pady=10, columnspan=2, sticky="nsew")

if __name__ == "__main__":
    app = App()
    app.mainloop()