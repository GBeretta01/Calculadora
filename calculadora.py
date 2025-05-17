from tkinter import Tk, Frame, Button, Entry, Label, Listbox
import csv
import os

class CalculadoraBasica:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora POO V2.1.0")
        self.historial = []
        self._configurar_ventana()
        self._crear_widgets()
        self._crear_bindings()

    def _configurar_ventana(self):
        self.root.configure(bg="#525252")
        self.root.resizable(False, False)

        for i in range(3):
            self.root.grid_rowconfigure(i, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

    def _crear_widgets(self):
        self.frame_superior = Frame(self.root, bg="#A3A3A3")
        self.frame_superior.grid(row=0, column=0, padx=4, pady=4, sticky="nsew", columnspan=4)

        self.btn_hist = Button(
            self.frame_superior,
            text="Hist",
            font=("Consolas", 14),
            bg="#525252",
            fg="white",
            command=self.mostrar_historial
        )
        self.btn_hist.grid(row=0, column=0, padx=2, pady=2, sticky="nsew")

        self.pantalla = Entry(
            self.root,
            font=("Consolas", 20),
            justify="right",
            bd=10,
            insertwidth=4,
            bg="#525252",
            fg="white"
        )
        self.pantalla.grid(row=1, column=0, columnspan=4, sticky="nsew", padx=4, pady=4)

        self.frame_botones = Frame(self.root, bg="#A3A3A3")
        self.frame_botones.grid(row=2, column=0, padx=4, pady=4, sticky="nsew", columnspan=4)
        self._crear_botones_numericos()

    def _crear_bindings(self):
        self.pantalla.bind("<Return>", lambda e: self.calcular_resultado())
        self.pantalla.bind("<Delete>", lambda e: self.borrar_pantalla())

    def _crear_botones_numericos(self):
        botones = [
            ("C", 1, 1), ("<-", 1, 2), ("/", 1, 3),
            ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("*", 2, 3),
            ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("-", 3, 3),
            ("1", 4, 0), ("2", 4, 1), ("3", 4, 2), ("+", 4, 3),
            ("0", 5, 1), (".", 5, 2), ("=", 5, 3)
        ]

        comandos_especiales = {
            "<-": self.borrar_ultimo,
            "C": self.borrar_pantalla,
            "=": self.calcular_resultado
        }

        for i in range(4):
            self.frame_botones.grid_columnconfigure(i, weight=1)

        for texto, fila, columna in botones:
            btn = Button(
                self.frame_botones,
                text=texto,
                font=("Consolas", 14),
                bg="#525252",
                fg="white"
            )
            btn.grid(row=fila, column=columna, padx=2, pady=2, sticky="nsew")
            
            if texto in comandos_especiales:
                btn.configure(command=comandos_especiales[texto])
            else:
                btn.configure(command=lambda t=texto: self.click_boton(t))

    def click_boton(self, valor):
        contenido = self.pantalla.get()
        
        if valor in "+-*/=" and not contenido:
            return
        
        if valor in "+-*/." and contenido[-1] in "+-*/.":
            return
        
        if valor == "." and any(op in contenido for op in "+-*/"):
            parte = contenido.split(op)[-1] if (op := self._ultimo_operador(contenido)) else contenido
            if "." in parte:
                return
        
        self.pantalla.insert(END, valor)

    def _ultimo_operador(self, cadena):
        operadores = {"+", "-", "*", "/"}
        for c in reversed(cadena):
            if c in operadores:
                return c
        return None

    def borrar_ultimo(self):
        self.pantalla.delete(len(self.pantalla.get())-1, END)

    def borrar_pantalla(self):
        self.pantalla.delete(0, END)

    def calcular_resultado(self):
        try:
            expresion = self.pantalla.get()
            resultado = str(eval(expresion))
            self.pantalla.delete(0, END)
            self.pantalla.insert(0, resultado)
            self._guardar_en_historial(expresion, resultado)
        except:
            self.pantalla.delete(0, END)
            self.pantalla.insert(0, "ERROR")

    def _guardar_en_historial(self, expresion, resultado):
        if not os.path.exists("historial.csv"):
            with open("historial.csv", "w", newline="", encoding="utf-8") as f:
                f.write("expresion,resultado\n")
                
        with open("historial.csv", "a", newline="", encoding="utf-8") as f:
            f.write(f"{expresion},{resultado}\n")

    def mostrar_historial(self):
        self.frame_botones.grid_remove()
        
        self.frame_historial = Frame(self.root, bg="#A3A3A3")
        self.frame_historial.grid(row=2, column=0, padx=4, pady=4, sticky="nsew", columnspan=4)

        Label(self.frame_historial,
            text="Historial (últimas 10 operaciones):",
            font=("Consolas", 12),
            bg="#A3A3A3", fg="white").grid(row=0, column=0, pady=5, columnspan=2)

        self.lista_hist = Listbox(self.frame_historial,
            width=30,
            height=8,
            font=("Consolas", 12),
            bg="#525252",
            fg="white")
        self.lista_hist.grid(row=1, column=0, padx=5, pady=5)

        Button(self.frame_historial,
            text="Volver",
            font=("Consolas", 12),
            bg="#525252",
            fg="white",
            command=self._ocultar_historial).grid(row=2, column=0, pady=5)

        self._actualizar_historial()

    def _ocultar_historial(self):
        self.frame_historial.grid_remove()
        self.frame_botones.grid()

    def _actualizar_historial(self):
        self.lista_hist.delete(0, END)
        try:
            with open("historial.csv", "r", encoding="utf-8") as f:
                lineas = list(csv.reader(f))[1:]  # Saltar encabezado
                for fila in reversed(lineas[-10:]):
                    self.lista_hist.insert(0, f"{fila[0]} = {fila[1]}")
        except FileNotFoundError:
            self.lista_hist.insert(0, "No hay historial disponible")

if __name__ == "__main__":
    root = Tk()
    app = CalculadoraBasica(root)
    root.mainloop()