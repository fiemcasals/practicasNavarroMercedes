
import random

anchoTablero = 10
tamanios_naves = [5, 4, 3, 3, 2]

def crear_tablero(ancho):
  tablero = []
  for i in range(ancho):
      fila = []
      for j in range(ancho):
          fila.append(0)
      tablero.append(fila)
  return tablero


def imprimir_tablero(tablero, ocultar_naves=False):
    letras = 'ABCDEFGHIJ'
    print("  " + " ".join(str(i) for i in range(anchoTablero)))
    for idx, fila in enumerate(tablero):
        linea = []
        for celda in fila:
            if ocultar_naves and celda == 1:
                linea.append("0")  # ocultar naves enemigas
            else:
                linea.append(str(celda))
        print(f"{letras[idx]} {' '.join(linea)}")
    print()

def posicionar_naves(tablero, tamanios_naves):
    for tamanio in tamanios_naves:
        colocada = False
        while not colocada:
            orientacion = random.choice(['H', 'V'])
            fila = random.randint(0, anchoTablero - 1)
            col = random.randint(0, anchoTablero - 1)

            if orientacion == 'H' and col + tamanio <= anchoTablero:
                if all(tablero[fila][col + i] == 0 for i in range(tamanio)):
                    for i in range(tamanio):
                        tablero[fila][col + i] = 1
                    colocada = True
            elif orientacion == 'V' and fila + tamanio <= anchoTablero:
                if all(tablero[fila + i][col] == 0 for i in range(tamanio)):
                    for i in range(tamanio):
                        tablero[fila + i][col] = 1
                    colocada = True

def traducir_coordenada(coordenada):
    letras = 'ABCDEFGHIJ'
    fila = letras.find(coordenada[0].upper())
    try:
        col = int(coordenada[1:])
    except ValueError:
        return -1, -1
    return fila, col

def disparar(tablero_enemigo, tablero_tiros, fila, col):
    if tablero_enemigo[fila][col] == 1:
        tablero_tiros[fila][col] = 'X'
        tablero_enemigo[fila][col] = 'X'
        print("¡Impacto!")
    else:
        tablero_tiros[fila][col] = '-'
        print("Agua.")

def coordenada_valida(fila, col):
    return 0 <= fila < anchoTablero and 0 <= col < anchoTablero

# Inicialización de tableros
miTableroTiros = crear_tablero(anchoTablero)
tableroTirosMaquina = crear_tablero(anchoTablero)
miTableroNaves = crear_tablero(anchoTablero)
tableroNavesMaquina = crear_tablero(anchoTablero)

# Posicionar naves
posicionar_naves(miTableroNaves, tamanios_naves)
posicionar_naves(tableroNavesMaquina, tamanios_naves)

# Juego por turnos
turno = 0
while True:
    print("\nTu tablero de tiros:")
    imprimir_tablero(miTableroTiros)
    print("Tu tablero de naves:")
    imprimir_tablero(miTableroNaves)

    # Turno del jugador
    while True:
        entrada = input("Ingresa coordenadas para disparar (ej: A5): ")
        fila, col = traducir_coordenada(entrada)
        if coordenada_valida(fila, col) and miTableroTiros[fila][col] == 0:
            disparar(tableroNavesMaquina, miTableroTiros, fila, col)
            break
        else:
            print("Coordenada inválida o ya disparaste ahí. Intenta de nuevo.")

    # Verificar si todas las naves enemigas fueron destruidas
    if not any(1 in fila for fila in tableroNavesMaquina):
        print("¡Ganaste! Todas las naves enemigas fueron destruidas.")
        break

    # Turno de la máquina
    while True:
        fila = random.randint(0, anchoTablero - 1)
        col = random.randint(0, anchoTablero - 1)
        if tableroTirosMaquina[fila][col] == 0:
            print(f"La máquina dispara en: {chr(65 + fila)}{col}")
            disparar(miTableroNaves, tableroTirosMaquina, fila, col)
            break

    # Verificar si todas tus naves fueron destruidas
    if not any(1 in fila for fila in miTableroNaves):
        print("¡Perdiste! La máquina destruyó todas tus naves.")
        break
