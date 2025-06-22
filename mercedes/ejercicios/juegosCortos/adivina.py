import random
numero = random.randint(1, 10)
intento = int(input("Adivina el número (1-10): "))
while intento != numero:
    if intento < numero:
        print("Muy bajo")
    else:
        print("Muy alto")
    intento = int(input("Intenta otra vez: "))
print("¡Correcto!")
