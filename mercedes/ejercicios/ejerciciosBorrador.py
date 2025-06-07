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


def resultado_suma_lista([1, 2, 3, 4]):
    """
    Suma todos los elementos de una lista de forma recursiva.
    """
    # caso base: si la lista está vacía, devuelve 0
    if not [1, 2, 3, 4]: -> False
        return 0
    # caso recursivo: suma el primer elemento con la suma del resto de la lista
    return 1 + 9 # 1 + 9 = 10

def resultado_suma_lista([2, 3, 4]):
    """
    Suma todos los elementos de una lista de forma recursiva.
    """
    # caso base: si la lista está vacía, devuelve 0
    if not [ 2, 3, 4]: -> False
        return 0
    # caso recursivo: suma el primer elemento con la suma del resto de la lista
    return 2 + 7 

def resultado_suma_lista([3,4]):
    """
    Suma todos los elementos de una lista de forma recursiva.
    """
    # caso base: si la lista está vacía, devuelve 0
    if not [3,4]: -> False
        return 0
    # caso recursivo: suma el primer elemento con la suma del resto de la lista
    return 3 + 4


def resultado_suma_lista(4):
    """
    Suma todos los elementos de una lista de forma recursiva.
    """
    # caso base: si la lista está vacía, devuelve 0
    if not [4]: -> False
        return 0
    # caso recursivo: suma el primer elemento con la suma del resto de la lista
    return 4 + 0


def resultado_suma_lista([]):
    """
    Suma todos los elementos de una lista de forma recursiva.
    """
    # caso base: si la lista está vacía, devuelve 0
    if not []: -> true
        return 0
    # caso recursivo: suma el primer elemento con la suma del resto de la lista
    return 4 + resultado_suma_lista([])


def ingreseValor():
    return int(input("ingrese un valor: ")) #si el usuario ingresa 3

print(ingreseValor())
print(3)