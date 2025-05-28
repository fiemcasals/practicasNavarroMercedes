
def suma(valor_anterior):
    if valor_anterior == 5:
        print(f"llegaste al final")
    else:
        valor_anterior += 1
        print(valor_anterior)
        suma(valor_anterior)


suma(0)

def tiro():
    fila = int(input("Fila (1-5): "))
    col = input("Columna (A-E): ").upper()
    

    if tablero_enemigo[fila][col] == 'E':
        print("💥 ¡Le diste a una nave enemiga!")
        
        tablero_enemigo[fila][col] = 'F'
    else:
        print("🌊 Agua.")
        tablero_tiros[fila][col] = '*'


