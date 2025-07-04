import tkinter as tk
from tkinter import messagebox
import random

class Buscaminas:
    def __init__(self, master, filas=8, columnas=8, cantidad_minas=10, vidas=1):
        self.master = master
        self.filas = filas
        self.columnas = columnas
        self.cantidad_minas = cantidad_minas
        self.vidas = vidas
        self.botones = [[None for _ in range(columnas)] for _ in range(filas)]
        self.tablero = [['0' for _ in range(columnas)] for _ in range(filas)]
        self.visible = [['#' for _ in range(columnas)] for _ in range(filas)]
        self.minas = set()

        self.generar_minas()
        self.calcular_numeros()
        self.crear_tablero()

    def generar_minas(self):
        while len(self.minas) < self.cantidad_minas:
            f = random.randint(0, self.filas - 1)
            c = random.randint(0, self.columnas - 1)
            self.minas.add((f, c))
        for f, c in self.minas:
            self.tablero[f][c] = '*'

    def calcular_numeros(self):
        for f in range(self.filas):
            for c in range(self.columnas):
                if self.tablero[f][c] == '*':
                    continue
                minas_cerca = 0
                for i in range(f - 1, f + 2):
                    for j in range(c - 1, c + 2):
                        if 0 <= i < self.filas and 0 <= j < self.columnas:
                            if self.tablero[i][j] == '*':
                                minas_cerca += 1
                self.tablero[f][c] = str(minas_cerca)

    def crear_tablero(self):
        for f in range(self.filas):
            for c in range(self.columnas):
                b = tk.Button(self.master, width=3, height=1,
                              command=lambda fila=f, col=c: self.click(fila, col))
                b.grid(row=f, column=c)
                self.botones[f][c] = b

    def click(self, fila, columna):
        if self.visible[fila][columna] != '#':
            return

        if self.tablero[fila][columna] == '*':
            self.botones[fila][columna].config(text='💣', bg='red')
            self.visible[fila][columna] = '*'
            self.vidas -= 1
            if self.vidas == 0:
                self.revelar_todo()
                messagebox.showinfo("Perdiste", "¡Pisaste una mina y te quedaste sin vidas! 😵")
                self.master.quit()
            else:
                messagebox.showwarning("¡Cuidado!", f"Pisaste una mina 💣. Te queda(n) {self.vidas} vida(s).")
            return

        self.propagacion(fila, columna)

        if self.juego_terminado():
            self.revelar_todo()
            messagebox.showinfo("¡Ganaste!", "¡Descubriste todas las casillas sin perder! 🎉")
            self.master.quit()

    def propagacion(self, fila, columna):
        if not (0 <= fila < self.filas and 0 <= columna < self.columnas):
            return
        if self.visible[fila][columna] != '#':
            return

        self.visible[fila][columna] = self.tablero[fila][columna]
        self.botones[fila][columna].config(text=self.tablero[fila][columna], relief=tk.SUNKEN)

        if self.tablero[fila][columna] == '0':
            vecinos = [(i, j) for i in range(fila - 1, fila + 2)
                               for j in range(columna - 1, columna + 2)
                               if (i, j) != (fila, columna) and 0 <= i < self.filas and 0 <= j < self.columnas]
            random.shuffle(vecinos)
            for i, j in vecinos[:random.randint(2, 5)]:
                self.propagacion(i, j)

    def juego_terminado(self):
        for f in range(self.filas):
            for c in range(self.columnas):
                if self.visible[f][c] == '#' and self.tablero[f][c] != '*':
                    return False
        return True

    def revelar_todo(self):
        for f in range(self.filas):
            for c in range(self.columnas):
                if self.tablero[f][c] == '*':
                    self.botones[f][c].config(text='💣', bg='red')
                else:
                    self.botones[f][c].config(text=self.tablero[f][c])


def main():
    root = tk.Tk()
    root.title("Buscaminas - Tkinter Edition")
    app = Buscaminas(root, filas=8, columnas=8, cantidad_minas=10, vidas=2)
    root.mainloop()

if __name__ == "__main__":
    main()
