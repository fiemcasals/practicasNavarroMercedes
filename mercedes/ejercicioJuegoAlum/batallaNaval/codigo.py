import random

# Definimos tamaño del tablero
FILAS = 5
COLUMNAS = ['A', 'B', 'C', 'D', 'E']
NAVES = 3  # cantidad de naves por jugador

# Crear tablero vacío (diccionario de diccionarios)
def crear_tablero():
    tablero = {}
    for i in range(1, FILAS + 1):
        tablero[i] = {}
        for letra in COLUMNAS:
            tablero[i][letra] = '0'  # 0 = agua
    return tablero

# Colocar naves aleatoriamente
def colocar_naves(tablero, simbolo): #el simbolo varia segun si es A(aliado) o E(enemigo)
    colocadas = 0 #es un contador que marca la cantidad de naves que se colocaron
    while colocadas < NAVES:
        fila = random.randint(1, FILAS) #siendo FILAS = 5, el rango es de 1 a 5
        col = random.choice(COLUMNAS)
        if tablero[fila][col] == '0': #esto descarta que se coloquen dos veces la nave en la misma posicion
            tablero[fila][col] = simbolo
            colocadas += 1

# Mostrar tablero con formato
def mostrar_tablero(tablero, ocultar=False):
    print("   " + "  ".join(COLUMNAS))
    for fila in range(1, FILAS + 1): #fila = 5
        print(f"{fila} ", end="")
        for col in COLUMNAS:
            val = tablero[fila][col]
            if ocultar and val == 'A':
                print(" 0", end=" ")
            else:
                print(f" {val}", end=" ")
        print()

# Preparación
tablero_jugador = crear_tablero()
tablero_enemigo = crear_tablero()
tablero_tiros = crear_tablero()  # para mostrar los disparos hechos al enemigo

colocar_naves(tablero_jugador, 'A')
colocar_naves(tablero_enemigo, 'E')

# Juego
print("🎯 ¡Bienvenido a Mini Batalla Naval!")
while True:
    print("\n¿Qué querés hacer?")
    print("1. Ver mis naves")
    print("2. Ver tablero de tiros")
    print("3. Disparar")
    print("4. Salir")

    opcion = input("Elegí una opción: ")

    if opcion == "1":
        print("\n🚢 Tus naves:")
        mostrar_tablero(tablero_jugador)
    elif opcion == "2":
        print("\n🎯 Tablero de tiros:")
        mostrar_tablero(tablero_tiros)
    elif opcion == "3":
        fila = int(input("Fila (1-5): "))
        col = input("Columna (A-E): ").upper()

        if tablero_enemigo.get(fila, {}).get(col) == 'E':
            print("💥 ¡Le diste a una nave enemiga!")
            tablero_tiros[fila][col] = 'X'
            tablero_enemigo[fila][col] = 'X'
        else:
            print("🌊 Agua.")
            tablero_tiros[fila][col] = '*'

        # Turno del enemigo (simple, aleatorio)
        while True:
            f = random.randint(1, FILAS)
            c = random.choice(COLUMNAS)
            if tablero_jugador[f][c] == 'A':
                tablero_jugador[f][c] = 'X'
                print(f"⚠️ ¡El enemigo acertó en {f}{c}!")
                break
            elif tablero_jugador[f][c] == '0':
                tablero_jugador[f][c] = '*'
                print(f"💨 El enemigo disparó a {f}{c} y falló.")
                break

    elif opcion == "4":
        print("🚪 ¡Gracias por jugar!")
        break
    else:
        print("❌ Opción inválida.")

    # Verificar fin del juego
    naves_enemigas = sum(row[col] == 'E' for row in tablero_enemigo.values() for col in row)
    naves_propias = sum(row[col] == 'A' for row in tablero_jugador.values() for col in row)

    if naves_enemigas == 0:
        print("🏆 ¡Ganaste! Hundiste todas las naves enemigas.")
        break
    if naves_propias == 0:
        print("💀 Perdiste... el enemigo hundió todas tus naves.")
        break
