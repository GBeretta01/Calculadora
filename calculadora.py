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

    pantalla.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=5, pady=5)

    botones_frame = Frame(root)
    botones_frame.grid(row=1, column=0, padx=5, pady=5)

    root.mainloop()

if __name__ == "__main__":
    interfaz_tkinter()