

diccionario = {"nombre": "Mercedes", "apellido": "Gonzalez", "edad": 25, "ciudad": "Buenos Aires"}
print(diccionario)
print(diccionario["nombre"])

diccionario["profesion"] = "Ingeniera"
print(diccionario)

diccionario["edad"] = 26
print(diccionario["edad"])

del diccionario["ciudad"]
print(diccionario)

#obtener todas las claves
print(diccionario.keys())

#obtener todos los valores
print(diccionario.values())

#obtener todos los items
print(diccionario.items())

#verificar si una valor esta en el diccionario
print("casals" in diccionario.values())

#verificar si una clave esta en el diccionario
print("nombre" in diccionario.keys())

#vamos a fusionar dos diccionarios
diccionario2 = {"nombre": "Mercedes", "apellido": "Gonzalez", "edad": 25, "ciudad": "Buenos Aires"}
diccionario3 = {"profesion": "Ingeniera", "pais": "Argentina"}
diccionario2.update(diccionario3)
print(diccionario2)


#recorrer un diccionario con un bucle

for clave, valor in diccionario2.items():
    print(f"{clave}: {valor}")
















