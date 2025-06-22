"""Escriba una función que reciba como parámetro el radio de un circulo y devuelva una tupla conteniendo 
en el primer elemento el perímetro y en el segundo el área del mismo.  
 
TIPs: Recuerde que la fórmula del perímetro es (2 * math.pi * r) y el área se define como (math.pi * r^2). Se puede 
utilizar la constante pi definida en el módulo math (import math) 
 
Resultado Esperado: Si se utiliza la funcion con el valor de r=5, entonces debe devolver la tupla (31.415, 
78.539)"""

import math

def calcular_circulo(radio):
    """Devuelve una tupla con el perímetro y el área de un círculo dado su radio."""
    perimetro = 2 * math.pi * radio
    area = math.pi * radio ** 2
    return (round(perimetro, 3), round(area, 3)) #round redonde en la cantidad de decimales que se le pasan, en este caso 3 decimales

# Ejemplo de uso:
resultado = calcular_circulo(5)
print(resultado)
