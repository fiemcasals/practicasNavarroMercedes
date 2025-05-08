"""
1. Usa random para generar operaciones aleatorias.

2. Varía el tipo de operación: +, -, *, /, //, **.

3. Calcula automáticamente el resultado correcto.

4. Ajusta los puntos ganados o perdidos según la dificultad de la operación.
"""

import random
import operator

# Inicialización de puntos
puntos = 30

# Definimos operaciones posibles y su dificultad relativa
operaciones = {
    '+': {'func': operator.add, 'ganar': 5, 'perder': 10},
    '-': {'func': operator.sub, 'ganar': 5, 'perder': 10},
    '*': {'func': operator.mul, 'ganar': 7, 'perder': 8},
    '/': {'func': operator.truediv, 'ganar': 10, 'perder': 6},
    '//': {'func': operator.floordiv, 'ganar': 10, 'perder': 6},
    '**': {'func': operator.pow, 'ganar': 15, 'perder': 3},
}

print("🎮 Bienvenido al Juego de Trivia Matemática 🎮")
print("Objetivo: llegar a 50 puntos respondiendo correctamente.")

# Bucle principal del juego
while puntos < 50:
    decision = input("\n¿Querés responder una pregunta? (sí / salir): ").lower()

    if decision == "salir":
        print("🛑 Saliste del juego.")
        break
    elif decision == "si":
        op = random.choice(list(operaciones.keys()))
        a = random.randint(1, 10)
        b = random.randint(1, 10 if op != '**' else 4) #probar cambiar el 4 por un random.randint(2,4)

        # Evitar divisiones por cero
        if op in ('/', '//'):
            while b == 0:
                b = random.randint(1, 10)

        resultado_real = operaciones[op]['func'](a, b)

        # Mostrar la operación
        pregunta = f"❓ ¿Cuánto es {a} {op} {b}?: "
        try:
            respuesta = float(input(pregunta))

            if round(respuesta, 2) == round(resultado_real, 2):
                puntos += operaciones[op]['ganar']
                print(f"✅ ¡Correcto! Ganaste {operaciones[op]['ganar']} puntos.")
            else:
                puntos -= operaciones[op]['perder']
                print(f"❌ Incorrecto. La respuesta era {resultado_real}. Perdiste {operaciones[op]['perder']} puntos.")
        except ValueError:
            print("⚠️ Ingresaste una respuesta inválida. Perdés 5 puntos por intento fallido.")
            puntos -= 5
    else:
        print("⚠️ Opción no válida. Escribí 'sí' o 'salir'.")
        continue

    # Mostrar puntaje actual
    print(f"🎯 Puntaje actual: {puntos}")

    # Verificar si perdió
    if puntos <= 0:
        print("💥 ¡Perdiste! Tu puntaje llegó a 0.")
        break

# Final del juego
if puntos >= 50:
    print("🏆 ¡Felicitaciones! Llegaste a 50 puntos y ganaste el juego.")
 

