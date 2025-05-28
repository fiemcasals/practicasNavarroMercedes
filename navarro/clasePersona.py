class Persona:

    def __init__(self, name, age):
        self.nombre = name
        self.edad = age
        

    def saludar(self):
        print(f"hola soy {self.nombre}, y tengo {self.edad}")

    def cumplir_anios(self):
        self.edad +=1

    
profesor = Persona("mauri", 34)
alumno1 = Persona("nico", 33)

    
"""clase -> plantilla
objeto -> plantilla completa con datos
atriburos -> datos
metodos -> funciones 

la clase (plantilla) se instancia(se completa) y genera un objeto(documento con datos) """

profesor.saludar()
alumno1.saludar()

