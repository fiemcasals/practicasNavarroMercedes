ciudades = ["Buenos Aires", "CABA", "La Plata", "Mar del Plata", "Rosario", "Córdoba", "Mendoza", "Salta", "Tucumán", "Neuquén"]

for ciudad in ciudades: 
    print(ciudad)

print("vamos con range")
for i in range(10):
    print(ciudades[i])

for indice, ciudad in enumerate(ciudades,  start=10):
    print(f"Ciudad {indice}: {ciudad}")

diccionario = {"nombre": "Mercedes", "apellido": "Gonzalez", "edad": 25, "ciudad": "Buenos Aires"}

for pais in diccionario.values():
    print(pais)

#explicar nuevamente: 

matriz = []
for i in range(3): # se tiene que repetir 3 veces
    fila = []
    for j in range(3):
        fila.append(i) #va  a ejecutar 3 veces esta linea <- en total se va a ejecutar 9
        #[0]
        #[0,1]
        #[0,1,2]
        # el vector llamado fila va a salir de este for como [0,1,2]
    matriz.append(fila)
    #matriz originalmente []
    #sumo fila
    #[[0,1,2]]

    #en la segunda vuelta matriz = [[0,1,2]]
    #cuando sumo -> [ [0,1,2], [0,1,2] ]
    #               [ lista1 , lista2   ]

    #en la tercera vuelta matriz = [ [0,1,2], [0,1,2] ]
    #cuando sumo -> [ [0,1,2], [0,1,2], [0,1,2] ]
    #               [ lista1 , lista2 , lista3  ]

"veamoslo como un humano"
#[ lista1 , lista2 , lista3  ]

"""
[ [0,1,2], 
  [0,1,2], 
  [0,1,2] ]
"""
                   

matriznueva = [ [0,1,2], [0,1,2], [0,1,2] ]
print(f" esta es la nueva matriz: {matriznueva}")
print("terminamos la impresion")


  
"""
📊 Desarrollo paso a paso
i	j	fila	                    matriz
0	0	[0]	                            []
0	1	[0, 0]	                        []
0	2	[0, 0, 0]	                    []
0	-	-	                        [[0, 0, 0]]
1	0	[1]                     	[[0, 0, 0]]
1	1	[1, 1]	                    [[0, 0, 0]]
1	2	[1, 1, 1]	                [[0, 0, 0]]
1	-	-	                        [[0, 0, 0], [1, 1, 1]]
2	0	[2]	                        [[0, 0, 0], [1, 1, 1]]
2	1	[2, 2]	                    [[0, 0, 0], [1, 1, 1]]
2	2	[2, 2, 2]	                [[0, 0, 0], [1, 1, 1]]
2	-	-	                        [[0, 0, 0], [1, 1, 1], [2, 2, 2]]
"""



#matriz = [[fila1], [fila2], [fila3]]
#print(matriz)

#imprimir la matriz
"""for i in range(3):
    for j in range(3):
        print(matriz[i][j], end=" ")
    print() 
"""

#salto a for/forInLine.py