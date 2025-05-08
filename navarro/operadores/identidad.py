
#voy a declarar una lista
lista = [1, 2, 3, 4, 5]

#voy a copiar la referencia en una nueva variable
lista2 = lista

#imprimo lista
print("lista:", lista)
#imprimo lista2
print("lista2:", lista2)
#modifico lista2
lista2[0] = 100
#imprimo lista2
print("lista2:", lista2)
#imprimo lista
print("lista:", lista)
lista3 = lista2
#imprimo lista3
print("lista3:", lista3)

direccionDeJuan= "calle falsa 123"
#voy a declarar otra variable con el nombre de direccionDeLaMamaDeJuan
direccionDeLaMamaDeJuan = direccionDeJuan
#imprimo la direccion de Juan
print("direccion de Juan:", direccionDeJuan)
#imprimo la direccion de la mama de Juan
print("direccion de la mama de Juan:", direccionDeLaMamaDeJuan)


a = [1,2,3 ]
b = a
print("a:", a)
print("b:", b)
c = [1,2,3]
print("c:", c)

print( a is b)
print( a is c)

print(a[2])