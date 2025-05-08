

ciudades = ["Buenos Aires", "CABA", "La Plata", "Mar del Plata", "Rosario", "Córdoba", "Mendoza", "Salta", "Tucumán", "Neuquén"]
for ciudad in ciudades:
    print(ciudad, end="-")

for indice, ciudad in enumerate(ciudades):
    print(f"Ciudad {indice}: {ciudad}")

for i in range(10):
    print(i)

for i in range(30, 5, -3):
    print(i)

#declaramos un vector
vector = [1, 2, 3, 4, 5]

#lo recoremos usando el indice i
for i in range(len(vector)):
    print(vector[i])

print(vector[0])
print(vector[1])
print(vector[2])
print(vector[3])
print(vector[4])

#vamos a ver un ejemplo con nombres
#yo no se cuantos alumnos tengo
alumnos = ["Juan", "Pedro", "Maria", "Jose", "Ana"]

#recorremos el vector
for i in range(len(alumnos)):
    print(alumnos[i], end="------")

