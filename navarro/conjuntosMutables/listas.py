

a = list("hola")
print(a) # ['h', 'o', 'l', 'a']
print(a[0]) # h
print(a[1]) # o
print(a[2]) # l
print(a[3]) # a

print(a[-1]) # a
print(a[-2]) # l
print(a[-3]) # o
print(a[-4]) # h
print(a[0:2]) # ['h', 'o']
print(a[0:3]) # ['h', 'o', 'l']
print(a[0:4]) # ['h', 'o', 'l', 'a']
print(a[2:4]) # ['l', 'a']

a.append("!")
print(a) # ['h', 'o', 'l', 'a', '!']

a.insert(0, "H")
print(a) # ['H', 'h', 'o', 'l', 'a', '!']

a.insert(3, "L")
print(a) # ['H', 'h', 'o', 'L', 'l', 'a', '!']

a.insert(4, "nunca dije que tenia que estar en la lista")
print(a) # ['H', 'h', 'o', 'L', 'l', 'a', '!', 'A']

a.insert(5, 100)
print(a) # ['H', 'h', 'o', 'L', 'l', 'a', '!', 100]


copiaListaA = a 
print(copiaListaA) # ['H', 'h', 'o', 'L', 'l', 'a', '!', 100]
copiaListaA[0] = "HOLA"
print(copiaListaA) # ['HOLA', 'h', 'o', 'L', 'l', 'a', '!', 100]
print(a) # ['HOLA', 'h', 'o', 'L', 'l', 'a', '!', 100]

miVariable =100

#voy a hacer una copia de a en copia_a para modificar solo copia _a sin alterar a la lista a
copia_a = a.copy()
print(copia_a) # ['HOLA', 'h', 'o', 'L', 'l', 'a', '!', 100]
copia_a.insert(4, "hola")
print(copia_a) # ['HOLA', 'h', 'o', 'L', 'hola', 'l', 'a', '!', 100]
print(a) # ['HOLA', 'h', 'o', 'L', 'l', 'a', '!', 100]



listaCorta = a[0:5]
print(listaCorta) # ['HOLA', 'h', 'o', 'L', 'l']
listaCompleta = a[0:8]
print(listaCompleta) # ['HOLA', 'h', 'o', 'L', 'l', 'a', '!', 100]

#quiero ver el largo del vector
print(len(a)) # 8
#vamos a fucionar el uso de len para saber el largo del vector y hacer una copia
copiaConLen = a[0:len(a)]
print(copiaConLen) # ['HOLA', 'h', 'o', 'L', 'l', 'a', '!', 100]

#eliminar el ultimo elemento de la lista
a.pop()
print(a) # ['HOLA', 'h', 'o', 'L', 'l', 'a', '!']

#eliminar un indice de la lista
a.pop(0)
print("analicemos el resultado")
print(a) 
a.insert(3,a.pop(4))
print(a) 


print(a) # ['h', 'o', 'L', 'l', '!']


#lista desordenada
a = [2, 1, 4, 3]
a.sort()
print(a) # [1, 2, 3, 4]
a.sort(reverse=True)
print(a) # [4, 3, 2, 1]

a.append(100)
print(a) # [4, 3, 2, 1, 100]

#vamos  declarar dos listas
a = [1, 2, 3]
b = [4, 5, 6]
#vamos a fusionar las listas
a.extend(b)
print(a) # [1, 2, 3, 4, 5, 6]

#vamos a fusionar con pop
a = [1, 2, 3]
b = [4, 5, 6]
a.append(b)
a.append("hola ")
print(a) # [1, 2, 3, [4, 5, 6]]

print(a)
print(a.pop())
print(a) # [1, 2, 3, 'hola ']

lista= [1, 2, 3]
pregunto = input("que indice queres eliminar? ")
if not pregunto.isdigit():
    print("no es un numero")
else:
    print("el valor que vos eliminaste es ", lista.pop(int(pregunto)))


