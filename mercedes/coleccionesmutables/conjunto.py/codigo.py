

conjunto_a = {1, "hol","hola", 3, 4 , 5}

conjuntoPalabras = {"a", "b", "aa" , "ab", "ac"}
print(conjuntoPalabras)
print(conjunto_a)

conjunto_a.add(6)
print(conjunto_a)

conjunto_a.add(1)
print(conjunto_a)

conjunto_a.add(8)
print(conjunto_a)

conjunto_a.add(7)
print(conjunto_a)

conjunto_a.add(7.5)
print(conjunto_a)

conjunto_a.add(6.5)
print(conjunto_a)


conjunto_a.add(0)
print(conjunto_a)


conjunto_a.add(-1)
print(conjunto_a)


conjunto_palabras = {"A", "B", "chau", "AA"}
print(conjunto_palabras)

conjunto_a.remove(3)
print(conjunto_a)

#vamos con el discard
conjunto_a.discard(4)
conjunto_a.discard(4)
print(conjunto_a)

#union de conjunots
conjunto_b = {1, 2, 3, 4, 5}
conjunto_c = {6, 7, 8, 9, 10}
conjunto_d = conjunto_b.union(conjunto_c)
print(conjunto_d)

conjunto_e = conjunto_b | conjunto_c
print(conjunto_e)

#interseccion de conjuntos
conjunto_f = {1, 2, 3, 4, 5}
conjunto_g = {4, 5, 6, 7, 8}
conjunto_h = conjunto_f.intersection(conjunto_g)
print(conjunto_h)

#vamos a hacer la interseccion usando el &
conjunto_i = conjunto_f & conjunto_g
print(conjunto_i)

#diferencia de conjuntos
conjunto_i = {1, 2, 3, 4, 5}
conjunto_j = {4, 5, 6, 7, 8}
conjunto_k = conjunto_i.difference(conjunto_j)
print(conjunto_k)

#diferencia usando el -
conjunto_l = conjunto_i - conjunto_j
print(conjunto_l)

#diferencia usando el -
conjunto_ll = conjunto_j - conjunto_i
print(conjunto_ll)

#diferencia simetrica
conjunto_m = conjunto_i.symmetric_difference(conjunto_j)
print(conjunto_m)

# vamos a hacer la diferencia simetrica usando el ^
conjunto_n = conjunto_i ^ conjunto_j
print(conjunto_n)

lista = [1, 2, 3, 4, 5, 4 ,3 ,2, 1]
print(lista)
conjunto_lista = set(lista)
print(conjunto_lista)

#quiero pasar el conjunto a lista
lista_conjunto = list(conjunto_lista)
print(lista_conjunto)


#sintesis de conjuntos:
#no guarda valores duplicados
#los guarda ordenados
#su sintaxis es con llaves {}





