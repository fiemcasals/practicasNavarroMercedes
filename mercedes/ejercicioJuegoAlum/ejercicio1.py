""". Escribir  una  función  que  reciba  como  parámetros  el  inicio  y  fin  (inclusive)  de  un  rango  numérico.  La 
función debe: 
a. Imprimir en pantalla todos aquellos números que sean divisibles por 7 pero no sean divisibles 
por 5.  
b. Imprimir el mismo resultado anterior, pero separados por coma. 
 
Resultado Esperado: Por ejemplo, si se invoca con los parámetros 1 y 100 (puntos a y b) 
 7 
14 
21 
28 
42 
49 
56 
63 
77 
84 
91 
98 
 
7,14,21,28,42,49,56,63,77,84,91,98"""


def ingresar_numero(mensaje):
    while True:
        try:
            numero = int(input(mensaje))
            return numero
        except ValueError:
            print("Por favor, ingrese un número válido.")

def mostrar_reglas():
    print("Reglas del juego:")
    print("1. El jugador debe ingresar un número entre 1 y 100.")
    print("2. El juego mostrará los números divisibles por 7 pero no por 5.")
    print("3. Los números se mostrarán en dos formatos: uno por uno y otro separados por comas.")
    print("4. El juego finalizará cuando el jugador decida salir.")


def calcular_numeros_divisibles(inicio, fin):
    numeros_divisibles = []
    for i in range(inicio, fin + 1):
        if i % 7 == 0 and i % 5 != 0:
            
            numeros_divisibles.append(str(i))

    return numeros_divisibles

def mostrar_numeros(numeros_divisibles, salto_linea="cualquier_valor"):
    if salto_linea:
        for numero in numeros_divisibles:
            print(numero)
    else:
        string = ", ".join(numeros_divisibles)
        print(string)


    """for numero in numeros_divisibles:
        print(numero, end=" ")"""
        #string = ", ".join(numeros_divisibles)
    #print("\n" + string)
    

mostrar_reglas()
    
numeroPartida = ingresar_numero("Ingrese el número de partida (inicio): ")
numeroFin = ingresar_numero("Ingrese el número de fin: ")

numeros_divisibles = calcular_numeros_divisibles(numeroPartida, numeroFin)

mostrar_numeros(numeros_divisibles)


