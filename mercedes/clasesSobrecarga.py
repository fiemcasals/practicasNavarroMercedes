class Vector:
    
    def __init__(self, x, y):
        """ Inicializa un vector en 2D con coordenadas (x, y) """
        self.x = x
        self.y = y

    def __add__(self, other):
        """ Sobrecarga del operador + para sumar dos vectores """
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        """ Sobrecarga del operador - para restar dos vectores """
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        """ Sobrecarga del operador * para escalar un vector """
        return Vector(self.x * scalar, self.y * scalar)

    def __truediv__(self, scalar):
        """ Sobrecarga del operador / para dividir un vector por un escalar """
        if scalar == 0:
            raise ValueError("No se puede dividir por cero")
        return Vector(self.x / scalar, self.y / scalar)

    def __mod__(self, scalar):
        """ Sobrecarga del operador % para calcular el módulo de cada componente """
        return Vector(self.x % scalar, self.y % scalar)

    def __eq__(self, other):
        """ Sobrecarga del operador == para comparar dos vectores """
        return self.x == other.x and self.y == other.y

    def __lt__(self, other):
        """ Sobrecarga del operador < para comparar la magnitud de dos vectores """
        return self.magnitud() < other.magnitud()

    def __le__(self, other):
        """ Sobrecarga del operador <= para comparar la magnitud de dos vectores """
        return self.magnitud() <= other.magnitud()

    def magnitud(self):
        """ Calcula la magnitud del vector (norma euclidiana) """
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def __str__(self):
        """ Define la representación en cadena del objeto """
        return f"Vector({self.x}, {self.y})"


lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
        
# Uso del operador + para concatenar listas
resultado_suma = lista1 + lista2
print("Concatenación con '+':", resultado_suma) #Concatenación con '+': [1, 2, 3, 4, 5, 6]
        
# Uso del operador * para repetir elementos
resultado_multiplicacion = lista1 * 3 #[1,2,3]* 3 #en este caso no es una clase con sobrecarga de operador
print("Repetición con '*':", resultado_multiplicacion) #Repetición con '*': [1, 2, 3, 1, 2, 3, 1, 2, 3]
        
# No todos los operadores estan definidos por defectos. A continuacion se detallan

# Pruebas con la clase Vector
v1 = Vector(2, 3)
v2 = Vector(4, 5)

# Suma de vectores
print("Suma:", v1 + v2)  # Vector(6, 8)

# Resta de vectores
print("Resta:", v1 - v2)  # Vector(-2, -2)

# Producto por un escalar
print("Multiplicación por escalar:", v1 * 2)  # Vector(4, 6)

# División por un escalar
print("División por escalar:", v2 / 2)  # Vector(2.0, 2.5)

# Módulo de cada componente con un escalar
print("Módulo:", v2 % 3)  # Vector(1, 2)

# Comparaciones entre vectores
print("¿Son iguales?", v1 == v2)  # False
print("¿v1 es menor que v2?", v1 < v2)  # True (porque la magnitud de v1 es menor)
print("¿v1 es menor o igual que v2?", v1 <= v2)  # True



print(v1)  # Output: Vector(6, 8) #esto tambien es una sobrecarga de operador. print imprime el valor de una variable o un string cuando el contenido entre los parentesis se encuentra entre comillas. Pero en este caso va hasta el metodo __str__ que redefine el comportamiento de print y le dice que imprimir


"""Conclusión 🚀

💡 La sobrecarga de operadores en Python es extremadamente útil en casos donde se trabaja con estructuras matemáticas complejas como vectores, matrices, fracciones, fechas, etc.
En este caso, aplicamos la sobrecarga a la clase Vector, lo que permite usar operadores como +, -, *, /, %, ==, < y <= de manera intuitiva en operaciones vectoriales.

¿Se pueden sobrecargar más operadores?
✅ Sí, hay más operadores que se pueden sobrecargar, como +=, -=, [], in, &, |, etc., dependiendo de las necesidades de la clase. Python nos da flexibilidad para hacer que nuestras clases sean más expresivas y fáciles de usar. 😃"""