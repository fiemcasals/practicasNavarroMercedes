
#tablero de barcos propio
#idem del Eno

#tablero de tiros propios

def crear_tablero(filas, columnas):
    return [["0" for _ in range(columnas)] for _ in range(filas)]

def imprimir_tablero(tablero):
    for fila in tablero:
        for pos in fila:
            if pos == "x":
                print(pos, end=" ")
            else:
                print("0", end=" ")

     

tablero_barcos_propios = crear_tablero(10 , 10)
tablero_barcos_eno = crear_tablero(10 , 10)

tablero_tiros_propios = crear_tablero(10 , 10)

