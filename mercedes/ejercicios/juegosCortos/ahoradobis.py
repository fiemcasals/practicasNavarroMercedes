import random

def verificar_vidas():
    #verifico a oculto, especificamente si existe algun '_'
    return vidas > 0

def verificar_oculta():
    return '_' in oculta

def verificarLetra(vidas):
    if letraSeleccionada in palabraSeleccionada:
        for posicion, letra in enumerate(palabraSeleccionada):
            if letraSeleccionada == letra:
                return posicion
    else:
        vidas -=1
        print(f"letra incorrecta, acaba de perder una vida, le queda {vidas}")
        listaLetrasSeleccionadas.append(letraSeleccionada)
        #return -1
        return verificarLetra(pedirLetraJugador())
        
            
def pedirLetraJugador():
    letra = input("ingrese una letra: ")
    #chequeo si el usuario ingreso un caracter
    if len(letra) != 1 or not letra.isalpha():
        print("debes ingresar un solo caracter")
        pedirLetraJugador()
    else:
        return letra.lower()

def mostrarEstadoSinAtributos():
    print(" ".join(oculta))
    print(" ".join(listaLetrasSeleccionadas))

listaPalabras = ['hola']#'tartamudo', 'leon', 'mascota', 'ahorcado'
#elementos del juego
#palabra_a_adivinar = input("ingrese una palabra a adivinar")

palabraSeleccionada = random.choice(listaPalabras)
#podemos hacer una lista y con el random.choice seleccionar una de la lista
#podemos hacer que el sistema ingrese la palabra con alguna libreria
#vamos a ingresar las letras para adivinar la palabra
#vamos a almacenar letra por letra
listaLetrasSeleccionadas = [] #iniciamos una lista vacia
oculta = ["_" for _ in palabraSeleccionada]

#vidas = 5
vidas = int(input("ingrese la cantidad de vidas: "))

#muestro el estado de mi palabra a adivinar
#creo una funcion para mostrar

#mostrarEstado(oculta,listaLetrasSeleccionadas) #no es necesario pasar las variables


while verificar_vidas() and verificar_oculta():
    mostrarEstadoSinAtributos()
    #le pedimos una letra al jugador
    letraSeleccionada = pedirLetraJugador()
    posicion = verificarLetra(vidas)
    if posicion != -1:
        oculta[posicion]=palabraSeleccionada[posicion]

if not verificar_oculta():
    print("ganaste")
else:
    print("perdiste")





