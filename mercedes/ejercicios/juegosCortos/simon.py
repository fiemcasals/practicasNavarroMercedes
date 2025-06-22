import random
import time

# Lista extendida de colores
colores = [
    "rojo", "azul", "verde", "amarillo", "naranja",
    "violeta", "rosa", "marrón", "negro", "blanco",
    "celeste", "turquesa", "gris", "beige", "bordó",
    "lima", "magenta", "cian", "dorado", "plateado"
]

# Secuencia del juego
secuencia = []

# Hasta 15 pasos en total (puede fallar en cualquier momento)
for ronda in range(1, 16):
    nuevo = random.choice(colores)
    secuencia.append(nuevo)

    print(f"\nRonda {ronda} - Memoriza la secuencia:")
    for color in secuencia:
        print(color)
        time.sleep(0.6)
    print("\n" * 30)  # "Limpia" pantalla

    respuesta = input("Repite la secuencia (colores separados por espacio): ").lower().split()

    if respuesta != secuencia:
        print("¡Incorrecto!")
        print(f"La secuencia correcta era: {' '.join(secuencia)}")
        break
else:
    print("¡Felicidades! Completaste las 15 rondas con éxito.")
