import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter
import random


'''
Nombre: Anibal Caeiro

[comentar la línea 36 o 50
Que serian los print(self.seleccion_cpu)

Piedra, Papel o Tijera (v 1.0):
    Al comenzar el juego generaremos un número RANDOM del 1 al 3 para la selección de la máquina, siendo 1 para “piedra”, el 2 para “papel” y 3 para “tijera”.
	El jugador seleccionará mediante uno de los botones su opción  y le informaremos si ganó, empató o perdió
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

    
        #print(self.seleccion_cpu)

    '''
    Piedra, Papel o Tijera (v 1.0):
    Al comenzar el juego generaremos un número RANDOM del 1 al 3 para la selección de la máquina, siendo 1 para “piedra”, el 2 para “papel” y 3 para “tijera”.
	El jugador seleccionará mediante uno de los botones su opción  y le informaremos si ganó, empató o perdió
    '''
    

    ready_player_one = question(title="", message="Ready Player One")
    if(ready_player_one == False):
        exit()
    else:
        nombre_jugador = prompt(title="", prompt="Ingresa tu nombre")
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
                else:
                    print("Tijera")
    
    def btn_piedra_on_click(self):
        self.numero_elegido = 1
        if(self.numero_random == 1):
            print("Los dos sacamos papel\nTuviste suerte {0}, hemos empatado....\nDesempatemos".format(self.nombre_jugador))
        elif(self.numero_random == 2):
            print("Come tierra {0}\n Te ganeeeeee\nPapel envuelve la piedra".format(self.nombre_jugador))
        else:
            print("La piedra rompe las tijeras\nMe ganaste {0}\n Tuviste mucha suerte".format(self.nombre_jugador))
        self.deshabilitar_botones()
        

    def btn_papel_on_click(self):
        self.numero_elegido = 2
        if(self.numero_random == 1):
            print("Me ganaste {0}\n Tuviste suerte".format(self.nombre_jugador))
        elif(self.numero_random == 2):
            print("Los dos sacamos papel\nTuviste suerte {0}, hemos empatado....\nDesempatemos".format(self.nombre_jugador))
        else:
            print("Come tierra {0}\n Te ganeeeeee\nPapel envuelve la piedra".format(self.nombre_jugador))
        self.deshabilitar_botones()

    def btn_tijera_on_click(self):
        self.numero_elegido = 3
        if(self.numero_random == 1):
            print("Come tierra {0}\n Te ganeeeeee\nPapel envuelve la piedra".format(self.nombre_jugador))
        elif(self.numero_random == 2):
            print("Me ganaste {0}\n Tuviste suerte".format(self.nombre_jugador))
        else:
            print("Los dos sacamos papel\nTuviste suerte {0}, hemos empatado....\nDesempatemos".format(self.nombre_jugador))
        self.deshabilitar_botones()
        pass

    def btn_restart_on_click(self):
        self.btn_piedra.configure(state="normal")
        self.btn_papel.configure(state="normal")
        self.btn_tijera.configure(state="normal")
        self.cpu_elije()
        

if __name__ == "__main__":
    app = App()
    app.mainloop()