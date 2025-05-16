from tkinter import *
from tkinter import ttk

def interfaz_tkinter():
    root = Tk()
    root.title("Calculadora V1.0.0")
    root.resizable(0,0)

    pantalla = Entry(
        root,
        font= ("Consolas",20),
        justify="right",
        bd = 10,
        insertwidth=4,
        background="#B6B6B6"
    )

    pantalla.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=4, pady=4)

    botones_frame = Frame(root)
    botones_frame.grid(row=1, column=0, padx=5, pady=5)

    botones = [
                            ("C",0,2),("<-",0,3),                 
        ("7",1,0),("8",1,1),("9",1,2),("/",1,3),
        ("4",2,0),("5",2,1),("6",2,2),("*",2,3),
        ("1",3,0),("2",3,1),("3",3,2),("-",3,3),
                  ("0",4,1),          ("=",4,3)
    ]

    for (num, x, y) in botones:
        boton = Button(
            botones_frame,
            text=num,
            font=("Consolas",14),
            #command=lambda t=num: click_boton(t)
        )
        boton.grid(row=x, column=y, padx=2, pady=2)

    root.mainloop()

if __name__ == "__main__":
    interfaz_tkinter()