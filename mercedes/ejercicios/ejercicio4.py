"""Escribir un programa que reciba como parámetro un string de elementos separados por coma y retorne 
una lista conteniendo cada elemento.  
 
Resultado Esperado: Si se utiliza como parámetro el string '14,Juana Perez,True' se espera 
que la función retorne la lista ['14' , 'Juana Perez', 'True']"""

""""
def separar_elementos(cadena):
    return cadena.split(',')

# Ejemplo de uso
resultado = separar_elementos('14,Juana Perez,True')
print(resultado)



#analizamos el mismo metodo sin usar split
"""
"""
def separar_elementos(cadena):
    lista = []
    elemento = ''
    
    for caracter in cadena:
        if caracter == ',':
            lista.append(elemento)
            elemento = ''
        else:
            elemento += caracter
    lista.append(elemento)  # Agrega el último elemento
    
    return lista

# Ejemplo de uso
resultado = separar_elementos('14,Juana Perez,True')
print(resultado)"""





"""
datos = "Juan,30,María,25,Carlos,40"
i = 0
elemento = ""
lista = []

while i < len(datos):
    if datos[i] == ",":
        lista.append(elemento)
        elemento = ""
    else:
        elemento += datos[i]
    i += 1

# Agregar el último elemento que no termina con coma
if elemento:
    lista.append(elemento)

# Ahora lista contiene todos los elementos separados
print(lista)
"""




string = "hola-como,andas+todo,bien"
#print(string[0])
#quieor separar por el caracter "," y "+" y "-"
stringNuevo = string.split(",")
for palabra in stringNuevo:
    print(palabra)


