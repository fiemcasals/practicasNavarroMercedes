import random
opciones = ["piedra", "papel", "tijera"]
jugador = input("Elige piedra, papel o tijera: ")
maquina = random.choice(opciones)
print(f"La máquina eligió: {maquina}")

if jugador == maquina:
    print("¡Empate!")
elif (jugador == "piedra" and maquina == "tijera") or \
     (jugador == "papel" and maquina == "piedra") or \
     (jugador == "tijera" and maquina == "papel"):
    print("¡Ganaste!")
else:
    print("Perdiste.")
