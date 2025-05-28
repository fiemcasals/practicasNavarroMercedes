"""
Enunciados de los 4 ejercicios recursivos que se desarrollan mas abajo script:



1. 🔢 Suma de elementos de una lista

Enunciado:
Implementar una función recursiva que reciba una lista de números y devuelva la suma total de sus elementos.
No se permite el uso de funciones iterativas ni funciones auxiliares como sum().

Ejemplo esperado:
suma_lista([1, 2, 3, 4]) → 10



2. 🧮 Contar elementos en una lista

Enunciado:
Definir una función recursiva que reciba una lista y devuelva la cantidad de elementos que contiene.
No se permite usar la función len() para contar elementos.

Ejemplo esperado:
contar_elementos([10, 20, 30, 40]) → 4



3. 🔁 Invertir una lista

Enunciado:
Escribir una función recursiva que reciba una lista y retorne una nueva lista con los mismos elementos en orden inverso.
No se permite utilizar ciclos ni funciones como reversed().

Ejemplo esperado:
invertir_lista([1, 2, 3]) → [3, 2, 1]



4. 🔤 Verificar si una palabra es palíndromo

Enunciado:
Crear una función recursiva que determine si una cadena de texto es un palíndromo (es decir, si se lee igual de izquierda a derecha que de derecha a izquierda).
No se permite invertir la cadena con slicing ni usar funciones auxiliares.

Ejemplos esperados:
es_palindromo("reconocer") → True
es_palindromo("hola") → False

"""
#el codigo empieza debajo del titulo "FUNCIONES RECURSIVAS SIMPLES"







# ================================
# FUNCIONES RECURSIVAS SIMPLES
# ================================

# 1. Sumar todos los elementos de una lista
def suma_lista(lista):
    # Caso base: si la lista está vacía, la suma es 0
    if not lista:
        return 0
    else:
        # Suma el primer elemento y llama recursivamente con el resto de la lista
        return lista[0] + suma_lista(lista[1:])

# 2. Contar la cantidad de elementos de una lista
def contar_elementos(lista):
    # Caso base: una lista vacía tiene 0 elementos
    if not lista:
        return 0
    else:
        # Cuenta el primer elemento y llama recursivamente con el resto
        return 1 + contar_elementos(lista[1:])

# 3. Invertir una lista
def invertir_lista(lista):
    # Caso base: una lista vacía ya está invertida
    if not lista:
        return []
    else:
        # Llama recursivamente con el resto de la lista y agrega el primer al final
        return invertir_lista(lista[1:]) + [lista[0]]

# 4. Verificar si una palabra es un palíndromo
def es_palindromo(palabra):
    # Caso base: si la palabra tiene 0 o 1 letra, es palíndromo
    if len(palabra) <= 1:
        return True
    # Si las letras de los extremos no coinciden, no es palíndromo
    elif palabra[0] != palabra[-1]:
        return False
    else:
        # Verifica la subcadena interna (sin los extremos)
        return es_palindromo(palabra[1:-1])

# ================================
# PRUEBAS DE CADA FUNCIÓN
# ================================
#if __name__ == "__main__":
if True:
    print("Suma de [1, 2, 3, 4]:", suma_lista([1, 2, 3, 4]))  # 10
    print("Cantidad de elementos en [10, 20, 30, 40]:", contar_elementos([10, 20, 30, 40]))  # 4
    print("Invertir [1, 2, 3]:", invertir_lista([1, 2, 3]))  # [3, 2, 1]
    print("¿'reconocer' es palíndromo?:", es_palindromo("reconocer"))  # True
    print("¿'hola' es palíndromo?:", es_palindromo("hola"))  # False
