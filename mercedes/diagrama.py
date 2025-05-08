# Número secreto fijo
numero_secreto = 7
intentos = 0

while intentos < 3:
    numero = int(input("Adivina el número (entre 1 y 10): "))
    
    if not numero.isdigit():
        print("Por favor, ingresa un número válido.")
        continue

    

    if numero == numero_secreto:
        print("¡Correcto! Ganaste.")
        break
    elif numero < numero_secreto:
        print("El número secreto es mayor.")
    else:
        print("El número secreto es menor.")
    
    intentos += 1

if intentos == 3 and numero != numero_secreto:
    print(f"Perdiste. El número era {numero_secreto}.")
