

import operator


diccionario = {"nombre": "Mercedes", "apellido": "Gonzalez", "edad": 25, "ciudad": "Buenos Aires"}
print(diccionario)
print(diccionario["nombre"])
diccionario["profesion"] = "Ingeniera"
#piso un valor
diccionario["edad"] = 26
print(diccionario["edad"])

del diccionario["ciudad"]
print(diccionario)

#imprimimos las claves
print(diccionario.keys())

#imprimimos los valores
print(diccionario.values())

#imprimimos los items
print(diccionario.items())

print("casals" in diccionario.values()) # False
print("nombre" in diccionario.keys()) # True



#fusionar dos diccionarios
diccionario2 = {"nombre": "Mercedes", "apellido": "Gonzalez", "edad": 25, "ciudad": "Buenos Aires"}
diccionario3 = {"profesion": "Ingeniera", "pais": "Argentina"}
diccionario2.update(diccionario3)
print(diccionario2) # {'nombre': 'Mercedes', 'apellido': 'Gonzalez', 'edad': 25, 'ciudad': 'Buenos Aires', 'profesion': 'Ingeniera', 'pais': 'Argentina'}

#vamos a recorre el diccionar con un for
for clave, valor in diccionario2.items():
    print(f"{clave}: {valor}")


operaciones = {
    '+': {'func': operator.add, 'ganar': 5, 'perder': 10},
    '-': {'func': operator.sub, 'ganar': 5, 'perder': 10},
    '*': {'func': operator.mul, 'ganar': 7, 'perder': 8},
    '/': {'func': operator.truediv, 'ganar': 10, 'perder': 6},
    '//': {'func': operator.floordiv, 'ganar': 10, 'perder': 6},
    '**': {'func': operator.pow, 'ganar': 15, 'perder': 3},
}
#print(operaciones)
print("\n ")
print(operaciones['*']["func"](2,3)) # 5