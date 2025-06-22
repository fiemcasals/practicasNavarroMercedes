# Tablero vacío
tablero = [" " for _ in range(9)]

# Función para mostrar el tablero
def mostrar_tablero():
    for i in range(0, 9, 3):
        print(f"{tablero[i]} | {tablero[i+1]} | {tablero[i+2]}")
        if i < 6:
            print("--+---+--")

# Verificar si alguien ganó
def hay_ganador(jugador):#0 X
    combinaciones = [
        (0,1,2), (3,4,5), (6,7,8),  # filas
        (0,3,6), (1,4,7), (2,5,8),  # columnas
        (0,4,8), (2,4,6)            # diagonales
    ]
    return any(tablero[a]==tablero[b]==tablero[c]==jugador for a,b,c in combinaciones)

# Juego principal
jugador_actual = "X"

for turno in range(9):
    mostrar_tablero()
    casilla = int(input(f"Jugador {jugador_actual}, elige una casilla (0-8): "))
    if tablero[casilla] != " ":
        print("Casilla ocupada, perdés el turno.")
    else:
        tablero[casilla] = jugador_actual
        if hay_ganador(jugador_actual):
            mostrar_tablero()
            print(f"¡Ganó el jugador {jugador_actual}!")
            break
        jugador_actual = "O" if jugador_actual == "X" else "X"
else:
    mostrar_tablero()
    print("¡Empate!")
