

class Persona:
    #metodos y atributos
    #sinonimo de un metodo es la funcion
    #sinonimo de un atributo es una variable

    #definir un metodo como una accion propia de la clase
    #constructor
    def __init__(self, nombre, edad, altura, nacionalidad, apellido, dni, peso):
        self.nombre = nombre
        self.edad = edad
        self.altura = altura
        self.nacionalidad = nacionalidad
        self.apellido = apellido
        self.dni = dni
        self.peso = peso
        #tambien puede iniciar los metodos
        self.saludar()

    #defino mi metodo saludar
    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre} {self.apellido} y tengo {self.edad} ")

    def cambiar_nombre(self, nuevo_nombre):
        #vamosa poner el nombre todo en mayuscula
        nuevo_nombre = nuevo_nombre.upper()
        self.nombre = nuevo_nombre

#clase -> plantillas
#instancia o instanciacion -> es el proceso de crear un objeto a partir de una clase 
#objeto -> es la plantilla o mejor dicho la clase personalizada
#funciones -> son acciones
#atributos -> son las variables o datos que tiene una plantilla u objeto
#variables -> es un espacio en memoria que guarda un dato puntual

#vamos a instanciar una clase(es decir una plantilla)
profesor = Persona("Mauricio", 34, 1.82, "argentino", "Casals", "35493060", 80)

#el profesor va a saludar
profesor.saludar()

profesor.cambiar_nombre(input("Ingrese el nuevo nombre del profesor: "))

print(profesor.nombre)