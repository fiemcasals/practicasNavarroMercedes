"""

ciudades = ["Buenos Aires", "CABA", "La Plata", "Mar del Plata", "Rosario", "Córdoba", "Mendoza", "Salta", "Tucumán", "Neuquén"]

for ciudad in ciudades:
    print(ciudad)

for i in range(10):
    print(ciudades[i])

for indice, ciudad in enumerate(ciudades,  start=100):
    print(f"Ciudad {indice}: {ciudad}")

diccionario = {"nombre": "Mercedes", "apellido": "Gonzalez", "edad": 25, "ciudad": "Buenos Aires"}

for pais in diccionario.values():
    print(pais)
"""
"""#quiero una matriz de 3x3
matriz = [[0 for j in range(3)] for i in range(3)]"""

#quiero una matriz de 3x3 mas amigable
matriz = []
for i in range(3):
    for j in range(3):
        matriz[i][j]= 0
        
#imprimir la matriz
for i in range(3):
    for j in range(3):
        print(matriz[i][j], end=" ")
    print() 


