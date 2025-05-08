
def saludar():
    print("Hola, bienvenido a la función básica de Python")


saludar()

# quiero un ejemplo de una funcion pasando un argumento
def saludar_nombre():
    nombre = input("Ingrese su nombre: ")
    print(f"Hola, {nombre}, bienvenido a la función básica de Python")


saludar_nombre()


# quiero un ejemplo de una funcion pasando dos argumentos

def saludar_nombre_y_edad(nombre, edad):
    print(f"Hola, {nombre}, bienvenido a la función básica de Python. Tienes {edad} años.")

saludar_nombre_y_edad("Juan", 30)


# quiero una funcion que retorne un valor
def sumar(a, b):
    return a + b

resultado = sumar(2, 3)
print(f"La suma de 2 y 3 es {resultado}")

# quiero un ejemplo de una funcion pasando un argumento
def saludar_nombre(nombre):
    print(f"Hola, {nombre}, bienvenido a la función básica de Python")


saludar_nombre("Juan")

#quiero un funcion que devuelva dos valores
def sumar_y_restar(a, b):
    suma = a + b
    resta = a - b
    return suma, resta

resultado_suma, resultado_resta = sumar_y_restar(5, 3)
print(f"La suma de 5 y 3 es {resultado_suma}")
print(f"La resta de 5 y 3 es {resultado_resta}")

# quiero una funcion que devuelva un diccionario
def crear_persona(nombre, edad):
    persona = {
        "nombre": nombre,
        "edad": edad
    }
    return persona


persona = crear_persona("Juan", 30)
print(f"La persona es {persona['nombre']} y tiene {persona['edad']} años")

# quiero una funcion que devuelva un string para ser impreso desde el script pricipal con un valor
def crear_mensaje(nombre, edad):
    return f"Hola, {nombre}, tienes {edad} años."


print(crear_mensaje("Juan", 30))
# quiero un ejemplo de una funcion pasando un argumento

