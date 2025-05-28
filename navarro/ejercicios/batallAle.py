import random

#creo el mapa
def crear_tablero():
    # Crear una matriz de 5x5 llena de ceros
    #vamos a usar dos for anidados
    filas = 5
    columnas = 5
    tablero = {}
    for i in range(filas):
        for j in range(columnas):
            tablero[i,j]= 0

    return tablero

def mostrar_tablero(tablero):
    # Mostrar el tablero
    print("\n")
    for i in range(5):
        for j in range(5):
            print(tablero[i,j], end=" ")
        print()

def colocar_barcos(tablero, cantidadDeBarcos, bando):
    while cantidadDeBarcos > 0:
        columna = random.randint(0, 4)
        fila = random.randint(0, 4)
        if tablero[columna,fila] == 0:
            tablero[columna,fila]= bando
            cantidadDeBarcos -= 1

def tiro():
    columa = int(input("Ingrese la columna: entre 0 y 4 "))
    fila = int(input("Ingrese la fila: entre 0 y 4"))
    if tableroEnemigo[columa,fila] == "E":
        print("Tiro acertado")
        tableroTiroEfectuados[columa,fila]= "X"
    else:
        print("Tiro fallido")
        tableroTiroEfectuados[columa,fila]= "-"
    mostrar_tablero(tableroTiroEfectuados)

    #tira la maquina
    columna = random.randint(0, 4)
    fila = random.randint(0, 4)
    if tableroAliado[columna,fila] == "A":
        print("La maquina te pego")
        tableroAliado[columna,fila]= "X"
    else:
        print("La maquina fallo")
        tableroAliado[columna,fila]= "-"
    mostrar_tablero(tableroAliado)
    

tableroAliado =crear_tablero()
tableroEnemigo = crear_tablero()
tableroTiroEfectuados = crear_tablero()
# Mostrar el tablero inicial
#mostrar_tablero(tablero)

# Definir la cantidad de barcos
cantidadDeBarcos = 5

colocar_barcos(tableroAliado, cantidadDeBarcos, "A")
colocar_barcos(tableroEnemigo, cantidadDeBarcos, "E")
mostrar_tablero(tableroAliado)
#mostrar_tablero(tableroEnemigo)

tira = 's'
while tira == 's':
    
    tiro()
    tira= input("Desea tirar nuevamente? (s/n): ")

print("Fin del juego")
