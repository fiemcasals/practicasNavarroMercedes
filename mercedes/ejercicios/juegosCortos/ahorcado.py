palabra = "gato"
oculta = ["_"] * len(palabra)
vidas = 5

while vidas > 0 and "_" in oculta:
    print(" ".join(oculta))
    letra = input("Letra: ")
    if letra in palabra:
        for i in range(len(palabra)):
            if palabra[i] == letra:
                oculta[i] = letra
    else:
        vidas -= 1
        print(f"¡Incorrecto! Te quedan {vidas} vidas.")
print("¡Ganaste!" if "_" not in oculta else f"Perdiste. Era: {palabra}")
