from tkinter import *
from tkinter import Tk, Frame, Label, Button
import csv
import os

def calculadora_basica():

    def click_boton(valor):
        contenido_pantalla = pantalla.get()

        if valor in "/+*-=." and contenido_pantalla == "":
            return
        
        if valor in "+-*/." and contenido_pantalla[-1] in "+-*/=.":
            return
        
        if valor == "." and "." in contenido_pantalla.split("+")[-1].split("-")[-1].split("*")[-1].split("/")[-1]:
            return
    
        pantalla.insert(END, valor)

    def borrar_num():
        contenido_pantalla = pantalla.get()

        pantalla.delete(len(contenido_pantalla) - 1, END)

    def borrar_pantalla():
        pantalla.delete(0, END)

    def resultado_pantalla():
        try:
            expresion = pantalla.get()
            resultado = str(eval(expresion))
            pantalla.delete(0, END)
            pantalla.insert(0, resultado)
            guardar_historial(expresion, resultado)
        except:
            pantalla.delete(0, END)
            pantalla.insert(0, "ERROR")
    
    def guardar_historial(expresion, resultado):
        nombre_csv = "historial.csv"

        if not os.path.exists(nombre_csv):
            with open(nombre_csv, "w", newline="", encoding="utf-8") as archivo:
                writer = csv.writer(archivo)
                writer.writerow(["expresion", "resultado"])

        with open(nombre_csv, "a", newline="", encoding="utf-8") as archivo:
            writer = csv.writer(archivo)
            writer.writerow([expresion, resultado])

    def ver_historial():
        global frame_historial

        botones_frame.grid_remove()

        frame_historial = Frame(root, bg=("#a3a3a3"))
        frame_historial.grid(row=2, column=0, padx=4, pady=4, sticky="nsew", columnspan=4)

        Label(frame_historial, 
            text="Historial (últimas 10 operaciones):", 
            font=("Consolas", 12), 
            bg="#A3A3A3", fg="white").grid(row=0, column=0, pady=5, columnspan=2)

        lista_hist = Listbox(frame_historial, 
                width=30, 
                height=8, 
                font=("Consolas", 12),
                bg="#525252", 
                fg="white"
                )
        lista_hist.grid(row=1, column=0, padx=5, pady=5)

        Button(frame_historial,
               text="Volver",
               font=("Consolas",12),
               bg=("#525252"),
               fg="white",
               command=lambda: [frame_historial.grid_remove(), botones_frame.grid()]
               ).grid(row=2,column=0,pady=5)
        
        try:
            with open("historial.csv", "r", encoding="utf-8") as archivo:
                lector = csv.reader(archivo)
                next(lector)
                lineas = list(lector)[-10:]

                for fila in reversed(lineas):
                    lista_hist.insert(0, f"{fila[0]} = {fila[1]}")

        except FileNotFoundError:
            lista_hist.insert(END, "No hay historial")

    root = Tk()
    root.title("Calculadora V2.0.0")
    root.resizable(0,0)
    root.configure(background="#525252")

    botones_cambio_frame = Frame(root)
    botones_cambio_frame.grid(row=0, column=0, padx=4, pady=4, sticky="nsew", columnspan=4)
    botones_cambio_frame.configure(background="#A3A3A3")

    botones_cambio = [
        ("Cient",0,0),
        ("Hist",0,1)
    ]

    for (bom,x,y) in botones_cambio:
        cambios = Button(
            botones_cambio_frame,
            text=bom,
            font=("Consolas",14),
            background="#525252",
            command= ver_historial if bom =="Hist" else None
        )
        cambios.grid(row=x, column=y, padx=2, pady=2, sticky="nsew")

    pantalla = Entry(
        root,
        font= ("Consolas",20),
        justify="right",
        bd = 10,
        insertwidth=4,
        background="#525252"
        )

    pantalla.grid(row=1, column=0, columnspan=4, sticky="nsew", padx=4, pady=4)

    botones_frame = Frame(root)
    botones_frame.grid(row=2, column=0, padx=4, pady=4, sticky="nsew", columnspan=4)
    botones_frame.configure(background="#A3A3A3")

    botones = [
                ("C",1,1),("<-",1,2),("/",1,3),                 
        ("7",2,0),("8",2,1),("9",2,2),("*",2,3),
        ("4",3,0),("5",3,1),("6",3,2),("-",3,3),
        ("1",4,0),("2",4,1),("3",4,2),("+",4,3),
                ("0",5,1),(".",5,2),("=",5,3)
        ]

    for i in range(4):  
        botones_frame.grid_columnconfigure(i, weight=1)  

    for (num, x, y) in botones:
        boton = Button(
            botones_frame,
            text=num,
            font=("Consolas",14),
            background="#525252"
        )
        boton.grid(row=x, column=y, padx=2, pady=2, sticky="nsew")

        if num == "<-":
            boton.configure(command=borrar_num)
        elif num == "C":
            boton.configure(command=borrar_pantalla)
        elif num == "=":
            boton.configure(command=resultado_pantalla)
        else:    
            boton.configure(command=lambda t=num: click_boton(t))


    root.mainloop()

if __name__ == "__main__":
    calculadora_basica()