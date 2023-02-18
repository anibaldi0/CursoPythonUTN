import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Nombre: Anibal Caeiro

Enunciado:
Al presionarse el boton 'Comenzar ingreso', solicitar mediante prompt todos los numero que el usuario quiera, hasta que presione el boton Cancelar del prompt o ingrese cero.

Acumular los valores positivos y multiplicar entre si aquellos que son negativos (*informar por terminal)

Determinar el maximo, el minimo y el promedio de todos los numeros ingresados.
e informarlos en los cuadros de textos txt_maximo, txt_minimo y txt_promedio respectivamente

- resolver usando lista

'''

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()
        
        # configure windows
        self.title("UTN FRA")

        self.txt_minimo = customtkinter.CTkEntry(master=self, placeholder_text="Minimo")
        self.txt_minimo.grid(row=0, padx=20, pady=20)

        self.txt_maximo = customtkinter.CTkEntry(master=self, placeholder_text="Maximo")
        self.txt_maximo.grid(row=1, padx=20, pady=20)

        self.txt_promedio = customtkinter.CTkEntry(master=self, placeholder_text="Promedio")
        self.txt_promedio.grid(row=2, padx=20, pady=20)

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=3, padx=20, pady=20, columnspan=2, sticky="nsew")

    '''
    Enunciado:
    Al presionarse el boton 'Comenzar ingreso', solicitar mediante prompt todos los numero que el usuario quiera, hasta que presione el boton Cancelar del prompt o ingrese cero.

    Acumular los valores positivos y multiplicar entre si aquellos que son negativos (*informar por terminal)

    Determinar el maximo, el minimo y el promedio de todos los numeros ingresados.
    e informarlos en los cuadros de textos txt_maximo, txt_minimo y txt_promedio respectivamente

    - resolver usando lista

    '''


    def btn_comenzar_ingreso_on_click(self):

        acumulador_general = 0
        acumulador_positivos = 0
        acumulador_multiplos_negativos = None
        suma_numeros_negativos = None
        contador_numeros_ingresados = 0
        promedio_numeros_ingresados = None
        maximo = None
        minimo = None
        lista_numeros_ingresados = [1,2,-1,-2]

        # ------------------------------------------------------------------------
        # codigo para ingresar numeros a la lista
        while (True):
            numero_ingresado_txt = prompt(title="", prompt="Ingrese un numero")
            if(numero_ingresado_txt != None and numero_ingresado_txt != "0"):
                numero_ingresado_int = int(numero_ingresado_txt)
                lista_numeros_ingresados.append(numero_ingresado_int)
            else:
                break
        # ------------------------------------------------------------------------
        # codigo para trabajar con la lista
        contador_numeros_ingresados = len(lista_numeros_ingresados)
        for numero in lista_numeros_ingresados:
            acumulador_general += numero
            if(numero > 0):
                acumulador_positivos += numero
            else:
                if(acumulador_multiplos_negativos == None):
                    acumulador_multiplos_negativos = numero
                    suma_numeros_negativos = numero
                else:
                    acumulador_multiplos_negativos *= numero
                    suma_numeros_negativos += numero

            if(maximo == None or maximo > numero):
                maximo = numero

            if(minimo == None or minimo < numero):
                minimo = numero
                
            promedio_numeros_ingresados = acumulador_general / contador_numeros_ingresados
            
        mensaje = "El ultimo numero ingresado es {0}\nLos numeros positivos suman: {1}\nLa suma negativos es {2}\nEl producto de numeros negativos es: {3}\nLa suma general es {4}\nEl maximo es {5}\nEl minimo es {6}\nEl promedio es: {7}\nSe contaron {8} numeros ingresados"
        mensaje = mensaje.format(numero, acumulador_positivos, suma_numeros_negativos, acumulador_multiplos_negativos, acumulador_general, minimo, maximo, promedio_numeros_ingresados, contador_numeros_ingresados)
        print(mensaje)


if __name__ == "__main__":
    app = App()
    app.mainloop()