class Persona: #clase
    def __init__(self, nombre, edad): #metodo
        self.nombre = nombre #atributo
        self.edad = edad #atributo

    def saludar(self): #metodo
        print(f"Hola, me llamo {self.nombre} y tengo {self.edad} años.")

    def cumplir_anios(self): #metodo
        self.edad += 1
        print(f"¡Feliz cumpleaños, {self.nombre}! Ahora tenés {self.edad} años.")
    
    def __str__(self):
        return f"El nombre de esta persona es: {self.nombre}, y su edad es:{self.edad})"

# Crear una persona
persona1 = Persona("Juan", 30) #llamamos al constructor
persona2 = Persona("Ana", 25) #llamando al constructor

# Usar los métodos
persona1.saludar()         # Hola, me llamo Juan y tengo 30 años.
persona1.cumplir_anios()   # ¡Feliz cumpleaños, Juan! Ahora tenés 31 años.

print("\nahora vamos con la perosna 2\n")
persona2.saludar()
persona2.cumplir_anios()

print("\nImprimiendo las personas\n")
print(persona1)  # Persona(nombre=Juan, edad=31)

