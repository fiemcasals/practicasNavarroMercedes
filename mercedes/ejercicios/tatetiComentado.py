#generar un tablero
#que dimensiones?
#3*3

#que estructura? matriz o un vector
#matriz 
"""
[
[" ", " ", " "],
[" ", " ", " "],
[" ", " ", " "]
]
"""
#tipo vector [" ", " ", " ", " ", " ", " ", " ", " ", " "]

#tablero tipo matriz
#tablero = [[" " for _ in range(3)] for _ in range(3)]
#tablero tipo vector
tablero = [" " for _ in range(9)]

def mostrar_tablero():
    #muestro tablero
    for i in range(0, 9, 3): # i -> 0, 3, 6
        print(f"{tablero[i]} | {tablero[i+1]} | {tablero[i+2]}")
        if i < 6:
            print("--+---+--")

#mientras se va jugando necesito verificar si hay un ganador
#posibles combinaciones de ganador
def hay_ganador(jugador): #X o O ->True o False 
    combinaciones = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # filas
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columnas
        (0, 4, 8), (2, 4, 6)              # diagonales
    ]
    return any(tablero[a] == tablero[b] == tablero[c] == jugador for a, b, c in combinaciones)
#any(True, False, False) -> True
#any(False, False, False) -> False
#any(False, True, False) -> True
#return 3>2 -> True
#return 3<2 -> False 
#tablero[a] == tablero[b] == tablero[c] == jugador #posibles valores del tablero -> combinaciones
#for combinacion in combinaciones - > las posibles tuplas: (0,1,2),(1,4,7)
#tablero[a] == tablero[b] == tablero[c] == jugador -> True o False
#en la primera tupla:
#tablero[0] == tablero[1] == tablero[2] == jugador -> "X" == "X" == "X" == Jugador -> Depende el jugador
#tablero[0] == tablero[1] == tablero[2] == jugador -> "X" == "X" == "X" == "X" -> True
#tablero[0] == tablero[1] == tablero[2] == jugador -> "X" == "O" == "X" == "X" -> False
#tablero[0] == tablero[1] == tablero[2] == jugador -> "X" == "X" == "X" == "O" -> False

#Declaramos un jugador para que este comience el juego
jugador_actual = "X" #este jugador comienza

#hay 9 lugares por ende hay 9 turnos
for turno in range (9):
    #Le mostramos el tablero para que sepa donde elegir
    mostrar_tablero()
    #Le pedimos al usuario o jugador que ingrese un valor entre 0 y 8. o prodriamos decir de 1 a 9 y nosotros le restamos una 
    casilla = int(input(f"Jugador {jugador_actual}, elige una casilla (0-8): "))
    #Verificamos si la casilla elegida esta ocupada
    if tablero[casilla] != " ":
        print("Casilla ocupada, elige otra casilla.")
    else:
        #si la casilla esta vacia, le asigno el valor del jugador actual
        tablero[casilla] = jugador_actual # tablero[ubicacion que eligio el jugador] = "x" o "O"
        #una vez que juego verifico si gane o no:
        if hay_ganador(jugador_actual):
            mostrar_tablero()
            print(f"¡Ganó el jugador {jugador_actual}!")
            break
        #cambio el turno del jugadora
        jugador_actual = "0" if jugador_actual == "X" else "X"
else:
    mostrar_tablero()
    print("¡Empate!")  # Si se completan los 9 turnos sin ganador, es un empate