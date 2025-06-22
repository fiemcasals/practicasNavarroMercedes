
def funcion(contador):
    if contador == 3:
        print("contador es 3")
        return

    contador +=1
    ciudades = ["Neuquen", "Mercedes"]
    for ciudad in ciudades:
        print(f"Contador: {contador}, Ciudad: {ciudad}")
        funcion(contador)


if __name__ == "__main__":
    # Ejemplo de uso
    print("Inicio de la función recursiva:")
     # Iniciar el contador en 0
    contador = 0
    funcion(contador)