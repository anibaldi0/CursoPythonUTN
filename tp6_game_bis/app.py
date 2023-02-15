import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter
import random
import time


'''
Nombre: Anibal
Apellido: Caeiro

Adivina el número (v 1.0):
Al comenzar el juego generamos un número secreto del 1 al 100, en la pantalla del juego dispondremos de un cuadro de texto 
para ingresar un número y un botón “Verificar”, si el número ingresado es el mismo que el número secreto se dará por terminado
el juego con un mensaje similar a este: 

En esta oportunidad el juego evaluará tus aptitudes a partir de la cantidad de intentos, por lo cual se informará lo siguiente:
    1° intento: “usted es un Psíquico”.
	2° intento: “excelente percepción”.
	3° intento: “Esto es suerte”.
	4° hasta 6° intento: “Excelente técnica”.
	Más de 6 intentos: “afortunado en el amor!!”.

de no ser igual se debe informar si 
“falta…”  para llegar al número secreto  o si 
“se pasó…”  del número secreto.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.txt_numero = customtkinter.CTkEntry(master=self)
        self.txt_numero.grid(row=0, column=1)

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        #self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")

        #fabricacion del boton reset
        self.btn_reset = customtkinter.CTkButton(master=self, text="Reset", command=self.btn_reset_on_click)
        #self.btn_reset.grid(row=3, pady=20, columnspan=2, sticky="nsew")

        self.inicio_juego()

        self.after(3000, self.mostrar_botones) #se llama a la funcion mostrar_botones para que los muestre a los 3 segundos

    #funcion que muestra los botones
    def mostrar_botones(self):
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")
        self.btn_reset.grid(row=3, pady=20, columnspan=2, sticky="nsew")
        self.after(3000, self.ocultar_botones) #se llama a la funcion ocultar_botones para que los oculte a los 3 segundos de mostrados

    #funcion que oculta los botones
    def ocultar_botones(self):
        self.btn_mostrar.grid_forget()
        self.btn_reset.grid_forget()


    #funcion que llama al boton reset
    def btn_reset_on_click(self):
        self.inicio_juego()

    def btn_mostrar_on_click(self):
        if(self.flag_play == True): # mientras sea True el codigo se ejecuta
            self.numero_intento = self.numero_intento + 1
            numero_ingresado_txt = self.txt_numero.get()
            numero_ingresado_int = int(numero_ingresado_txt)
            numero_secreto = self.numero_secreto
            mensaje2 = ""
            if(numero_ingresado_int == numero_secreto):
                ts_fin_juego = time.time()
                tiempo_de_juego =  int(ts_fin_juego - self.ts_inicio_juego)
                match(self.numero_intento):
                    case 1 :
                        mensaje2 = '"usted es un Psíquico"\nGanaste el juego en {0} segundos'.format(tiempo_de_juego)
                    case 2 :
                        mensaje2 = '“excelente percepción”\nGanaste el juego en {0} segundos'.format(tiempo_de_juego)
                    case 3 :
                        mensaje2 = '“Esto es suerte”\nGanaste el juego en {0} segundos'.format(tiempo_de_juego)
                    case 4 | 5 | 6 :
                        mensaje2 = '“Excelente técnica”\nGanaste el juego en {0} segundos'.format(tiempo_de_juego)
                    case _ :
                        mensaje2 = '“afortunado en el amor!!”\nGanaste el juego en {0} segundos'.format(tiempo_de_juego)
                mensaje = "Ganaste en {0} intentos\n{1}".format(self.numero_intento, mensaje2)
                self.flag_play == False #para que deje de ejecutarse el codigo
            elif(numero_ingresado_int > numero_secreto):
                mensaje = "Te pasaste"
            else:
                mensaje = "Falta"

            alert(title="", message=mensaje)

    def inicio_juego(self): #funcion que define el reset
        self.numero_secreto = random.randrange(1, 100)
        #si la variable flag esta en False, no nos permite ingrasar al codigo, no nos permite jugar
        self.flag_play = True #esta variable muestra en que estado esta el juego (jugando o no jugando)
        self.numero_intento = 0
        print(self.numero_secreto)
        self.txt_numero.delete(0, 100)
        self.ts_inicio_juego = time.time()


if __name__ == "__main__":
    app = App()
    app.mainloop()