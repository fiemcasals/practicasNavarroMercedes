# Clase básica para entender funciones comunes de numpy y su equivalente en Python puro

"""
| Característica           | `list` (Python)   | `np.array` (NumPy)                   |
| ------------------------ | ----------------- | ------------------------------------ |
| Tipos de datos           | Heterogéneos      | Homogéneos                           |
| Velocidad                | Lenta             | Muy rápida                           |
| Operaciones matemáticas  | No vectorizadas   | Vectorizadas                         |
| Métodos avanzados        | No (solo básicos) | Sí (estadísticos, álgebra, etc.)     |
| Uso de memoria           | Alto              | Eficiente                            |
| Soporte multidimensional | Limitado          | Total (vectores, matrices, tensores) | #tensor -> multiples dimensiones
"""

# Simulamos importar numpy como np
import numpy as np

class NumpyVsPython:
    def crear_array_np(self, lista):
        """
        Crea un array de numpy desde una lista
        """
        return np.array(lista) #recuerden que es distinto a una lista 

    def crear_array_puro(self, lista):
        """
        En Python puro, una lista ya es una estructura similar a un array
        """
        return list(lista)  # Devuelve la misma lista

    def suma_np(self, array):
        """
        Suma todos los elementos usando numpy
        """
        return np.sum(array)

    def suma_puro(self, lista):
        """
        Suma todos los elementos usando Python puro
        """
        total = 0
        for elemento in lista:
            total += elemento
        return total

    def media_np(self, array):
        """
        Calcula la media (promedio) con numpy
        """
        return np.mean(array)

    def media_puro(self, lista):
        """
        Calcula la media con Python puro
        """
        if len(lista) == 0:
            return 0
        return self.suma_puro(lista) / len(lista)

    def matriz_np(self, lista_de_listas):
        """
        Crea una matriz (2D array) con numpy
        """
        return np.array(lista_de_listas) #el comando es igual que para generar una array simil lista pero con distintos datos de entrada (lista de listas), lo que devuelve una matriz"
    def matriz_puro(self, lista_de_listas):
        """
        En Python puro, se representa igual como lista de listas
        """
        return [list(fila) for fila in lista_de_listas]

    def transponer_np(self, matriz):
        """
        Transpone una matriz con numpy
        """
        """
    A = [[1, 2, 3], 
         [4, 5, 6]]
    A^T = [[1, 4],
           [2, 5],
           [3, 6]]
        """
        return np.transpose(matriz)

    def transponer_puro(self, matriz):
        """
        Transpone una matriz con Python puro
        """
        return [list(fila) for fila in zip(*matriz)] #*valores desempaqueta la lista y pasa los elementos como argumentos separados a print.
        #zip(...)	Agrupa elementos por columna
        """
        zip([1, 2, 3],              
            [4, 5, 6],     
            [7, 8, 9])
                |
                |
            [
            (1, 4, 7),
            (2, 5, 8),
            (3, 6, 9)
            ]
        """

    def multiplicacion_elemento_a_elemento_np(self, a, b):
        """
        Multiplicación elemento a elemento con numpy de dos listas, ej a[0] * b[0], a[1] * b[1], etc.
        """
        return np.multiply(a, b)

    def multiplicacion_elemento_a_elemento_puro(self, a, b):
        """
        Multiplicación elemento a elemento con Python puro
        """
        return [x * y for x, y in zip(a, b)] #agrupa las columnas:
    """
a = [1, 2, 3]
b = [4, 5, 6]

list(zip(a, b))  # → [(1, 4), (2, 5), (3, 6)]
"""

# ===================== EJEMPLOS DE USO =====================
if __name__ == "__main__":
    obj = NumpyVsPython() #ver que init esta por defecto

    lista = [1, 2, 3, 4]
    lista2 = [10, 20, 30, 40]
    matriz = [[1, 2], [3, 4]]

    print("=== CREACIÓN DE ARRAYS ===")
    print("Numpy:", obj.crear_array_np(lista))
    print("Puro:", obj.crear_array_puro(lista))

    print("\n=== SUMA ===")
    print("Numpy:", obj.suma_np(lista))
    print("Puro:", obj.suma_puro(lista))

    print("\n=== MEDIA ===")
    print("Numpy:", obj.media_np(lista))
    print("Puro:", obj.media_puro(lista))

    print("\n=== MATRIZ ===")
    print("Numpy:", obj.matriz_np(matriz))
    print("Puro:", obj.matriz_puro(matriz))

    print("\n=== TRANSPUESTA ===")
    print("Numpy:", obj.transponer_np(matriz))
    print("Puro:", obj.transponer_puro(matriz))

    print("\n=== MULTIPLICACIÓN ELEMENTO A ELEMENTO ===")
    print("Numpy:", obj.multiplicacion_elemento_a_elemento_np(lista, lista2))
    print("Puro:", obj.multiplicacion_elemento_a_elemento_puro(lista, lista2))
