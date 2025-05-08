#juego
#calcular una operacion matematic
#el jugador parte con 30 puntos. si pasa los 50 gana si tiene menos de 0 pierde
#el jugador determina cuanto jugar 
#puede perder con un puntaje menor a cero
#cuando quiere terminar ve si gano o no



#variables -> puntos_del_jugador
#operaciones -> igual  jugador coin la respuesta del juego
# y si yo uso numeros random, tengo que hacer las operaciones
# condicionales -> para saber si gano o perdio
# ciclo -> while 
"""
if True:
    #me ejecuta siempre esta linea, pq la condicion siempre True
    # pero desp sale

if sueldo> 2000:
    #se ejecuta esta linea

while qres_jugar == "si":
    print("Hola")qres

print("terminaste el juego")"""


import random
# Genera un número entero aleatorio entre 1 y 10
numero = random.randint(1, 10)
print("Número aleatorio entre 1 y 10:", numero)

# generame dos numeros
numero2 = random.randint(1, 10)

# mostrame la suma de ambos numeros para que lo calcule
print("La suma de los dos numeros es:", numero + numero2)

#dame la opcion de calcularlo, y mostrame los numeros con un input
resultado_usuario = input(f"¿Cuanto es la suma de los dos numeros? {numero} + {numero2}")
resultado = numero + numero2

# veriquen usando condicionales si el resultado es igual al resultado del usuario
# generame numeros aleatorios con python

#voy a hacer un bloque para produtos
operacion ='*' #-> input
operacion = input("¿Que operacion queres hacer? (suma o multiplicacion): ")

