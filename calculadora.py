from tkinter import *
from tkinter import Tk, Frame, Label, Button

def click_boton(valor):
    contenido_pantalla = pantalla.get()

    if valor in "/+*-=" and contenido_pantalla == "":
        return
    
    if valor in "+-*/" and contenido_pantalla[-1] in "+-*/=":
        return
    
    pantalla.insert(END, valor)

root = Tk()
root.title("Calculadora V1.0.3")
root.resizable(0,0)
root.configure(background="#525252", bg="#525252")

pantalla = Entry(
    root,
    font= ("Consolas",20),
    justify="right",
    bd = 10,
    insertwidth=4,
    background="#525252"
    )

pantalla.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=4, pady=4)

botones_frame = Frame(root)
botones_frame.grid(row=1, column=0, padx=4, pady=4, sticky="nsew", columnspan=4)
botones_frame.configure(background="#A3A3A3")

botones = [
              ("C",0,1),("<-",0,2),("/",0,3),                 
    ("7",1,0),("8",1,1),("9",1,2),("*",1,3),
    ("4",2,0),("5",2,1),("6",2,2),("-",2,3),
    ("1",3,0),("2",3,1),("3",3,2),("+",3,3),
              ("0",4,1),          ("=",4,3)
    ]

for i in range(4):  
    botones_frame.grid_columnconfigure(i, weight=1)  

for (num, x, y) in botones:
    boton = Button(
        botones_frame,
        text=num,
        font=("Consolas",14),
        command=lambda t=num: click_boton(t),
        background="#525252"
    )
    boton.grid(row=x, column=y, padx=2, pady=2, sticky="nsew")

root.mainloop()