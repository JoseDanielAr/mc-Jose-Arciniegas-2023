import tkinter as tk
import math

class Calculadora(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Calculadora de operaciones trigonométricas")
        self.master.geometry("300x200")  # Cambia el tamaño de la ventana a 400x300 píxeles
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self, text="Ingrese su operación:")
        self.label.pack(side="top")

        self.input = tk.Entry(self)
        self.input.pack(side="top")

        self.res = tk.Label(self, text="")
        self.res.pack(side="bottom")

        self.calcular = tk.Button(self)
        self.calcular["text"] = "Calcular"
        self.calcular["command"] = self.calcular_operacion
        self.calcular.pack(side="left")

        self.salir = tk.Button(self)
        self.salir["text"] = "Salir"
        self.salir["command"] = self.master.destroy
        self.salir.pack(side="right")

    def calcular_operacion(self):
        op = self.input.get()
        try:
            fun, rad = op.split('(')
            rad = float(rad.replace(")", ""))
            if fun == "sen":
                res = math.sin(rad)
            elif fun == "cos":
                res = math.cos(rad)
            elif fun == "tan":
                res = math.tan(rad)
            elif fun == "sec":
                res = 1 / math.cos(rad)
            elif fun == "csc":
                res = 1 / math.sin(rad)
            else:
                res = "Operación incorrecta"
            self.res.config(text=res)
        except:
            self.res.config(text="Operación incorrecta.")

root = tk.Tk()
app = Calculadora(master=root)
app.mainloop()
