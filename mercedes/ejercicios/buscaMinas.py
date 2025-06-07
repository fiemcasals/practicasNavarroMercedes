import random

class Buscaminas:
    def __init__(self, filas, columnas, cantidad_minas):
        self.filas = filas
        self.columnas = columnas
        self.cantidad_minas = cantidad_minas
        self.tablero = [['0' for _ in range(columnas)] for _ in range(filas)]
        self.visible = [['#' for _ in range(columnas)] for _ in range(filas)]
        self.minas = set()# conjunto para evitar minas duplicadas
        self.generar_minas()
        self.calcular_numeros()

    def generar_minas(self):
        while len(self.minas) < self.cantidad_minas:
            fila = random.randint(0, self.filas - 1)
            columna = random.randint(0, self.columnas - 1)
            self.minas.add((fila, columna)) #el conjunto con el metodo add los ingresa de manera ordendada y evita duplicados
        for f, c in self.minas:
            self.tablero[f][c] = '*'

    def calcular_numeros(self):
        for fila in range(self.filas):
            for columna in range(self.columnas):
                if self.tablero[fila][columna] == '*':
                    continue
                minas_cerca = 0
                for nf in range(fila - 1,fila + 2):
                    for nc in range(columna -1,columna + 2):
                        if 0 <= nf < self.filas and 0 <= nc < self.columnas:
                            if self.tablero[nf][nc] == '*':
                                minas_cerca += 1
                self.tablero[fila][columna] = minas_cerca

    def mostrar_tablero(self):
        print("\nTablero:")
        print("    ", end="")
        for col in range(self.columnas):
            print(f"{col:2}", end=" ")
        print()
        for i, fila in enumerate(self.visible):
            print(f"{i:2}  ", end="")
            for celda in fila:
                print(f" {celda}", end=" ")
            print()

    def descubrir(self, fila, columna):
        if not (0 <= fila < self.filas and 0 <= columna < self.columnas):
            print("Coordenadas fuera del rango.")
            return True, 0

        if self.visible[fila][columna] != '#':
            print("Casilla ya descubierta.")
            return True, 0

        if self.tablero[fila][columna] == '*':
            self.visible[fila][columna] = '*'
            print("¡Pisaste una mina! 💥")
            return True, -1  # Perdió una vida

        self.propagacion(fila, columna)
        return True, 0

    def propagacion(self, fila, columna):
        if not (0 <= fila < self.filas and 0 <= columna < self.columnas):#si esta fuera del tablero retorna sin hacer nada 
            return
        if self.visible[fila][columna] != '#': #si ya fue descubierto retorna sin hacer nada
            return
        if self.tablero[fila][columna] != '*': #si no es una mina, lo descubre
            self.visible[fila][columna] = self.tablero[fila][columna]

        if self.tablero[fila][columna] == '0':
            vecinos = [(i, j) for i in range(fila - 1, fila + 2)
                               for j in range(columna - 1, columna + 2)
                               if (i, j) != (fila, columna) and 0 <= i < self.filas and 0 <= j < self.columnas]
            random.shuffle(vecinos)
            cantidad = random.randint(2, 5) #podemos acortar la cantidad de vecinos a descubrir
            for nf, nc in vecinos[:cantidad]:
                self.propagacion(nf, nc)

    def juego_terminado(self):
        for f in range(self.filas):
            for c in range(self.columnas):
                if self.visible[f][c] == '#' and self.tablero[f][c] != '*':
                    return False
        return True


def jugar():
    filas = int(input("Ingrese la cantidad de filas (recomendado 8): ") or 8)
    columnas = int(input("Ingrese la cantidad de columnas (recomendado 8): ") or 8)
    minas = int(input("Ingrese la cantidad de minas (recomendado 10): ") or 10)

    vidas = None
    while vidas is None:
        try:
            vidas = int(input("Ingrese la cantidad de vidas (recomendado 1 a 3): "))
            if vidas <= 0:
                print("Debe ingresar un número positivo.")
                vidas = None
        except ValueError:
            print("Ingrese un número válido.")

    juego = Buscaminas(filas, columnas, minas)

    while True:
        juego.mostrar_tablero()

        try:
            f = int(input("Seleccioná fila (0 a 7): "))
            c = int(input("Seleccioná columna (0 a 7): "))
        except ValueError:
            print("Entrada inválida. Ingrese números válidos.")
            continue

        seguir, resultado = juego.descubrir(f, c)
        if resultado == -1:
            vidas -= 1
            print(f"Te queda(n) {vidas} vida(s).")
            if vidas == 0:
                print("¡Te quedaste sin vidas! 😵 Fin del juego.")
                juego.mostrar_tablero()
                break

        if not seguir:
            break

        if juego.juego_terminado():
            juego.mostrar_tablero()
            print("¡Felicidades! Has descubierto todas las casillas sin pisar todas las minas. 🎉")
            break


if __name__ == "__main__":
    jugar()
