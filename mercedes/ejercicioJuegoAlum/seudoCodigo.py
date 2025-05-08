
#juego
#calcular una operacion matematica
#el jugador determina cuanto jugar 
#puede perder con un puntaje menor a cero
#cuando quiere terminar ve si gano o no


# "perdida de punto" -> en codigo -> 
#  if -> condicional -> determina si gano o perdio
# 

#el jugador determina cuanto jugar
# imprimir por pantalla si quiere jugar
# necesito un input 
# necesito la variable "respuesta_del_jugadora_si_continua"
# necesito un if -> para ver si es verdadera
# estructura de repeticion


#puede perder con un puntaje menor a cero
# variable donde guardo los puntos
# condicional materialzado por un if 
# imprimos por pantalla perdiste/ganaste


# vamos a armar el codigo

#  saludamos y mostramos instrucciones
# 
print("🎮 Bienvenido al Juego de Trivia 🎮") 

print("Objetivo: llegar a 50 puntos respondiendo correctamente.")


# pregunto si quire jugar/seguir jugando

decision = "si"
puntos = 30

while puntos < 50  and puntos > 0:
    # Pregunto si quiere responder una pregunta
    decision = input("\n¿Querés responder una pregunta? (sí / salir): ").lower()
    
    if decision == "salir":
        print("🛑 Saliste del juego.")
        break
    elif decision == "si":
        respuesta = input("❓ ¿Cuánto es 2 + 2?: ")
        
        if respuesta == "4":
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
    
# pregunto si es menor a cero, -> perdiste
print("gaste")
#else ->ganaste