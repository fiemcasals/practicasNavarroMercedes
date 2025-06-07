
# 2. Contar la cantidad de elementos de una lista
def contar_elementos(lista):
    # Caso base: una lista vacía tiene 0 elementos
    if not lista:
        return 0
    else:
        # Cuenta el primer elemento y llama recursivamente con el resto
        return 1 + contar_elementos(lista[1:])

lista= [1,2,3,4]
#quiero el metodo len para saber la cantidad de elmentos
#print(len(lista))

#vamos a contar los elementos mediante una iteracion usando for
"""contador = 0
for i in lista:
    contador +=1

print("La cantidad de elementos de la lista es:", contador)"""

