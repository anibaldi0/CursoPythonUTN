import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter
import random


'''
Nombre: Anibal Caeiro

Piedra, Papel o Tijera (v 2.0):
    Al comenzar el juego generaremos un número RANDOM del 1 al 3 para la selección de la máquina, siendo 1 para “piedra”, el 2 para “papel” y 3 para “tijera”.
	El jugador seleccionará mediante uno de los botones su opción  y le informaremos si ganó, empató o perdió

Ahora debemos informar cuantas veces se ganó, perdió o empató
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.btn_piedra = customtkinter.CTkButton(master=self, text="Piedra", command=self.btn_piedra_on_click)
        self.btn_piedra.grid(row=2, pady=10, columnspan=2, sticky="nsew")

        self.btn_papel = customtkinter.CTkButton(master=self, text="Papel", command=self.btn_papel_on_click)
        self.btn_papel.grid(row=3, pady=10, columnspan=2, sticky="nsew")

        self.btn_tijera = customtkinter.CTkButton(master=self, text="Tijera", command=self.btn_tijera_on_click)
        self.btn_tijera.grid(row=4, pady=10, columnspan=2, sticky="nsew")

        self.btn_restart = customtkinter.CTkButton(master=self, text="RESTART", command=self.btn_restart_on_click, fg_color="red")
        self.btn_restart.grid(row=5, pady=20, columnspan=2, sticky="nsew")
        
        self.cpu_elije()
        #print(self.seleccion_cpu)

    def deshabilitar_botones(self):
        self.btn_piedra.configure(state="disabled")
        self.btn_papel.configure(state="disabled")
        self.btn_tijera.configure(state="disabled")
        
        #self.contador_vitorias_cpu = 0 
        #self.contador_vitorias_player_1 = 0 
        self.contador_gana_player_one = 0
        self.contador_gana_la_pc = 0
        self.contador_empate = 0

    ready_player_one = question(title="", message="Ready Player One?")
    if(ready_player_one == False):
        exit()
    else:
        nombre_jugador = prompt(title="", prompt="Ingrese su nombre")
        if(nombre_jugador == None):
            exit()
        else:
            nombre_jugador = nombre_jugador.capitalize()
            
    def cpu_elije(self):
            self.numero_random = random.randint(1, 3)
            if(self.numero_random == 1):
                print("Piedra")
            elif(self.numero_random == 2):
                print("Papel")
            elif(self.numero_random == 3):
                print("Tijera")

    def btn_piedra_on_click(self):
        if(self.numero_random == 1):
            print("Empatamos")
        elif(self.numero_random == 2):
            print("Ganeeeee")
        else:
            print("Gano player one")
        #self.contadores()
        self.deshabilitar_botones()
        self.mensaje_alerta()

    def btn_papel_on_click(self):
        if(self.numero_random == 1):
            print("Gano player one")
        elif(self.numero_random == 2):
            print("Empatamos")
        else:
            print("Ganeeeee")
        #self.contadores()
        self.deshabilitar_botones()
        self.mensaje_alerta()

    def btn_tijera_on_click(self):
        if(self.numero_random == 1):
            print("Ganeeeee")
        elif(self.numero_random == 2):
            print("Gano player one")
        else:
            print("Empatamos")
        #self.contadores()
        self.deshabilitar_botones()
        self.mensaje_alerta()
        
    def mensaje_alerta(self):
        if((self.numero_random == 1 and self.nombre_jugador == 3) or (self.numero_random == 2 and self.nombre_jugador == 2) or (self.numero_random == 3 and self.nombre_jugador == 2)):
            self.gana_la_pc = "Te ganeeeeee...\nCome tierra {0}".format(self.nombre_jugador)
            self.mensaje = self.gana_la_pc
            #self.contador_gana_la_pc += 1
        elif((self.numero_random == 1 and self.nombre_jugador == 2) or (self.numero_random == 2 and self.nombre_jugador == 3) or (self.numero_random == 3 and self.nombre_jugador == 1)):
            self.gana_player_one = "Me ganaste {0}\nFue pura suerte...seguro me viste antes".format(self.nombre_jugador)
            self.mensaje = self.gana_player_one
            #self.contador_gana_player_one += 1
        elif(self.numero_random == self.nombre_jugador):
            self.empate = "Solo empatamos {0}...\nEn esta proxima te gano".format(self.nombre_jugador)
            self.mensaje = self.empate
            #self. contador_empate += 1
        alert(title="", message=self.mensaje)
                
        #alert(title="", message="La PC gano {0}\nEmpatamos {1}\n{2} ganaste {3} pero tuviste suerte".format(self.contador_gana_la_pc, self.contador_empate, self.nombre_jugador, self.contador_gana_player_one))
                    

    def contadores(self):
        pass

    def btn_restart_on_click(self):
        self.btn_piedra.configure(state="normal")
        self.btn_papel.configure(state="normal")
        self.btn_tijera.configure(state="normal")
        self.cpu_elije()
        #print(self.seleccion_cpu)


if __name__ == "__main__":
    app = App()
    app.mainloop()