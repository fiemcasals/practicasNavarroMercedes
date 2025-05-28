"""

#quiero imprimir el caracter correspondiente en ascci a cada letra
for i in range(97, 123):
    print(chr(i), i)     


#vamos a hacer dos for anidados
for i in range(97, 105):
    for j in range(97, 105):
        print(chr(i), chr(j))

#quiero transformar un caracter en un numero ascci
#ord('a') = 97
print(ord('a'))  # 97

for i in ['a','b','c','d','e']:
    print(i)

lista = ['a','b','c','d','e']
for i in lista:
    print(i)"""

for i in range(97, 101):
    for j in range(5):
        print(f"{chr(i)} : {j}")