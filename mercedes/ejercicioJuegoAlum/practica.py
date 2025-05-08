"""# Inicialización de puntos
puntos = 25

print("🎮 Bienvenido al Juego de Trivia 🎮")
print("Objetivo: llegar a 50 puntos respondiendo correctamente.")

# Bucle principal del juego
while puntos < 50:
    decision = input("\n¿Querés responder una pregunta? (sí / salir): ").lower()

    if decision == "salir":
        print("🛑 Saliste del juego.")
        break
    elif decision == "si" or decision == "sí":
        respuesta = input("❓ ¿Cuánto es 2 + 2?: ")
        
        if respuesta == "4": # "4" == "4"
            puntos += 10  # Operador de asignación compuesta
            print("✅ ¡Correcto! Ganaste 10 puntos.")
        else:
            puntos -= 5  # Operador de asignación compuesta
            print("❌ Incorrecto. Perdiste 5 puntos.")
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


print(f"🔚 Juego terminado. Puntaje final: {puntos}")

"""
"""
vector = ["Juan", "Pedro", "Maria", "Ana"]
diccionarios = {"Juan": 8, "Pedro": 7, "Maria": 9, "Ana": 6}
for i in vector:
    if diccionarios[i] < 7: #diccionarios[juan] == 8
        print(f"el alumno {i} no aprobo la diplomatura porque se saco un {diccionarios[i]}")
    else:
        print(f"el alumno {i} aprobo la diplomatura con un {diccionarios[i]}")


tupla = (1, 2, 3, 4, 5)
print(tupla)

tupla = (1, 2, 3, 4, 6)
print(tupla)
"""
