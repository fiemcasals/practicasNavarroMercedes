

## 🧑‍🏫 Clase: Slicing en Python


### 📌 ¿Qué significa la palabra "slicing"?

"""En inglés, "slice" significa rebanada o porción.
En programación, slicing es la técnica de extraer una parte (una rebanada) de una secuencia, como una lista, una cadena de texto (`str`), una tupla, etc."""



## ✂️ 1. Sintaxis básica


#secuencia[inicio:fin:paso] ->similar for 


#`inicio`: posición desde donde empezar (incluido).
#`fin`: posición donde terminar (excluido).
#`paso`: cada cuántos elementos avanzar (puede ser negativo).

## 🔡 2. Slicing con strings

"""
texto = "Python"
| Código        | Resultado  | Explicación                        |
| ------------- | ---------- | ---------------------------------- |
| `texto[0:2]`  | `'Py'`     | De índice 0 a 1                    |
| `texto[1:4]`  | `'yth'`    | De índice 1 a 3                    |
| `texto[:3]`   | `'Pyt'`    | Desde el inicio hasta índice 2     |
| `texto[3:]`   | `'hon'`    | Desde índice 3 hasta el final      |
| `texto[:]`    | `'Python'` | Copia completa                     |
| `texto[::2]`  | `'Pto'`    | Cada dos letras                    |
| `texto[::-1]` | `'nohtyP'` | Invertido (de atrás para adelante) |"""


## 📋 3. Slicing con listas

numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#numeros[2:6]     # [2, 3, 4, 5]
#numeros[:4]      # [0, 1, 2, 3]
#numeros[6:]      # [6, 7, 8, 9]
numeros[::3]     # [0, 3, 6, 9]
numeros[::-1]    # [9, 8, 7, ..., 0] (invertida)

#noten que se estan pisando a si mismos en el lugar
#verificamos imprimiendo el ultimo
print(numeros[::-1]) #deberia imprimir [9,6,3,0]

## ⚠️ 4. ¿Qué pasa si los índices se salen del rango?

#Python no lanza error si te pasás en slicing:


numeros = [1, 2, 3]

print(numeros[0:10])   # [1, 2, 3] — simplemente agarra lo que puede
numeros[10:]    # [] — devuelve lista vacía
print(numeros)



## 🧪 5. Ejemplo: Verificar palíndromo


def es_palindromo(palabra):
    return palabra == palabra[::-1]

es_palindromo("reconocer")   # True
es_palindromo("python")      # False


## 🧠 6. Truco útil: Copiar secuencias


lista = [1, 2, 3]
copia = lista[:]   # copia completa

print(lista == copia)       # True
print(lista is copia)       # False (diferente objeto)


## 🔁 7. Slicing con paso negativo

#Podés usar slicing de derecha a izquierda:

texto = "abcdef"

texto[::-1]     # 'fedcba'
texto[-3:]      # 'def' (últimos 3 caracteres)
#texto[-4:-1]    # 'cde' (de la 4ª última hasta la 2ª última)

print(texto) #declarando "texto[-3:]" le da valor a esa variable pero no pisa la original

## ✅ 8. Resumen visual


secuencia = ['a', 'b', 'c', 'd', 'e']
"""
índices    =   0    1    2    3    4
negativos  =  -5   -4   -3   -2   -1
"""

print(secuencia[1:4])   # ['b', 'c', 'd']
print(secuencia[-3:])   # ['c', 'd', 'e']
print(secuencia[::-1])  # ['e', 'd', 'c', 'b', 'a']




