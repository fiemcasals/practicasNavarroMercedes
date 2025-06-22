import random

pos_j1 = pos_j2 = 0
meta = 20

while pos_j1 < meta and pos_j2 < meta:
    input("Turno Jugador 1 (Enter para tirar dado)")
    pos_j1 += random.randint(1, 6)
    print(f"Jugador 1: {pos_j1}")

    input("Turno Jugador 2 (Enter para tirar dado)")
    pos_j2 += random.randint(1, 6)
    print(f"Jugador 2: {pos_j2}")

if pos_j1 >= meta:
    print("¡Jugador 1 gana!")
else:
    print("¡Jugador 2 gana!")
