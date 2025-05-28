"""1. 🔢 Suma de elementos de una lista

Enunciado:
Implementar una función recursiva que reciba una lista de números y devuelva la suma total de sus elementos.
No se permite el uso de funciones iterativas ni funciones auxiliares como sum().

Ejemplo esperado:
suma_lista([1, 2, 3, 4]) → 10"""

#invoco / defino una funcion
def resultado_suma_lista(lista):
    """
    Suma todos los elementos de una lista de forma recursiva.
    """
    # caso base: si la lista está vacía, devuelve 0
    if not lista:
        return 0
    # caso recursivo: suma el primer elemento con la suma del resto de la lista
    return lista[0] + resultado_suma_lista(lista[1:])

print(resultado_suma_lista([1, 2, 3, 4]))  # Salida: 10
"""

vector = [1, 2, 3, 4]
vector_copia = vector[1:3]  # Copia superficial
#vector_copia[0] = 10
print(vector_copia) # salida: [10, 2, 3, 4]
print(vector) # salida: [1, 2, 3, 4]
vector[2] = 20
print(vector) # salida: [1, 2, 20, 4]
print(vector_copia) # salida: [10, 2, 3, 4]"""



#invoco / defino una funcion

"""
print((resultado_suma_lista([1, 2, 3, 4])))  

def resultado_suma_lista([1, 2, 3, 4]):]):
    
    #Suma todos los elementos de una lista de forma recursiva.
    
    # caso base: si la lista está vacía, devuelve 0
    if not [1, 2, 3, 4]: -> False:
        return 0
    # caso recursivo: suma el primer elemento con la suma del resto de la lista
    return 1 + 9

def resultado_suma_lista([2, 3, 4]):]):
    
    #Suma todos los elementos de una lista de forma recursiva.
    
    # caso base: si la lista está vacía, devuelve 0
    if not [2, 3, 4]: -> False:
        return 0
    # caso recursivo: suma el primer elemento con la suma del resto de la lista
    return 2 + 7


def resultado_suma_lista([ 3, 4]):]):
    
    #Suma todos los elementos de una lista de forma recursiva.
    
    # caso base: si la lista está vacía, devuelve 0
    if not [3, 4]: -> False:
        return 0
    # caso recursivo: suma el primer elemento con la suma del resto de la lista
    return 3 + 4

def resultado_suma_lista([4])):
    
    #Suma todos los elementos de una lista de forma recursiva.
    
    # caso base: si la lista está vacía, devuelve 0
    if not [4]: -> False:
        return 0
    # caso recursivo: suma el primer elemento con la suma del resto de la lista
    return 4 + 0

def resultado_suma_lista([])):
    
    #Suma todos los elementos de una lista de forma recursiva.
    
    # caso base: si la lista está vacía, devuelve 0
    if not []: -> False:
        return 0
    # caso recursivo: suma el primer elemento con la suma del resto de la lista
    return 4 + resultado_suma_lista([])"""