
#no puede repetir valores
conjuntos_a = {1, 2, 3}
conjuntos_b = {1, 2, 3, 4, 5}

#agregar un elemento
print(conjuntos_a) # {1, 2, 3}
conjuntos_a.add(4)
print(conjuntos_a) # {1, 2, 3, 4}

#eliminar un elemento
print(conjuntos_a) # {1, 2, 3, 4}
conjuntos_a.remove(4)
print(conjuntos_a) # {1, 2, 3}

#eliminar un elemento que no existe
#conjuntos_a.remove(5) # KeyError: 5
#print(conjuntos_a) # {1, 2, 3}


#eliminar un elemento que no existe sin error
conjuntos_a.discard(5) # no hace nada
print(conjuntos_a) # {1, 2, 3}

#eliminar un elemento aleatorio
print(conjuntos_a) # {1, 2, 3}
conjuntos_a.pop() # elimina un elemento aleatorio
print(conjuntos_a) # {2, 3} o {1, 3} o {1, 2} dependiendo del elemento eliminado

#defino dos conjuntos para hacer operaciones entre ellos
conjuntos_a = {1, 2, 3}
conjuntos_b = {3, 4, 5}

#unir conjuntos
conjuntos_c = conjuntos_a.union(conjuntos_b)
print(conjuntos_c) # {1, 2, 3, 4, 5}

#union por el operador |
conjuntos_c = conjuntos_a | conjuntos_b
print(conjuntos_c) # {1, 2, 3, 4, 5}

#interseccion
conjuntos_c = conjuntos_a.intersection(conjuntos_b)
print(conjuntos_c) # {3}

#interseccion por el operador &
conjuntos_c = conjuntos_a & conjuntos_b
print(conjuntos_c) # {3}

#diferencia entre conjuntos
print("\ndiferencia de conjuntos\n")
conjuntos_c = conjuntos_a.difference(conjuntos_b)
print(conjuntos_c) # {1, 2}

conjunto_x = {5 , 6, 7}
conjunto_y = {6, 7, 8}

#yo te voy a pasar un conjunto de numeros, despues te paso otro conjunto y os fijate que valores se repiten en ambos conjuntos, esos valores que repiten eliminalos del primer conjunto

conjuntos_yy = conjunto_x - conjunto_y
print(conjuntos_yy) # {5}

#diferencia simetrica

print(f"conjunto_a: {conjuntos_a}")
print(f"conjunto_b: {conjuntos_b}")
conjuntos_c = conjuntos_a.symmetric_difference(conjuntos_b)
print(conjuntos_c) # {1, 2,4, 5 }

lista_de_alumnos = ["Juan", "Pedro", "Maria", "Juan", "Pedro", "Maria"]
conjunto_alumnos = set(lista_de_alumnos)
print(conjunto_alumnos) # {'Juan', 'Pedro', 'Maria'}
#quiero pasar nuevamente a lista
lista_de_alumnos = list(conjunto_alumnos)
print(lista_de_alumnos) # ['Juan', 'Pedro', 'Maria']



#quiero hacer una diferencia simetrica entre dos conjuntos, diferenciadas por grupo
grupo_a = {1, 2, 3, 4, 5}
grupo_b = {4, 5, 6, 7, 8}
print("indice de una lista")
print(lista_de_alumnos[1])


#resto el conjunto b al conjunto a
grupo_c = grupo_a - grupo_b
#imprimo nuevo conjunto avisando que es la diferencia simetrica del conjunto a
print(f"Diferencia simetrica entre grupo_a y grupo_b, perteneciente unicamente al grupo_a: {grupo_c}") # {1, 2, 3}

#repito el proceso para el grupo_b
grupo_d = grupo_b - grupo_a
#imprimo nuevo conjunto avisando que es la diferencia simetrica del conjunto b
print(f"Diferencia simetrica entre grupo_b y grupo_a, perteneciente unicamente al grupo_b: {grupo_d}") # {6, 7, 8}