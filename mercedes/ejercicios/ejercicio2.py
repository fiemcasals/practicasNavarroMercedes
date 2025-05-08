"""2. Escribir la función factorial, que reciba como parámetro el numero inicial y compute su resultado.  
a. Ejemplo factorial(8) = 8*7*6*5*4*3*2*1 = 40320. Recuerde que factorial de 0 por definición es 1.  
b. Hacer la implementación inversa (si lo hizo recursivo, hacerlo iterativo o viceversa) """

numero = int(input("Ingrese un número para calcular su factorial: "))

def factorial_iterativo(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

def factorial_recursivo(n):
    if n == 0:
        return 1
    else:
        return n * factorial_recursivo(n - 1)

