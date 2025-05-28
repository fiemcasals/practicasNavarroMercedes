

def factorial_recursivo(n):
    if n == 0:
        return 1
    else:
        return n * factorial_recursivo(n - 1)

print(24)#ingreso el 4

def factorial_recursivo(4):
    if 4 == 0: #4 == 0 -> False
        return 1 #no se ejecuta la linea
    else:
        return 4 * 6
    
    #segunda vez que llama a la funcion
def factorial_recursivo(3):
    if 3 == 0: #3 == 0 -> False
        return 1 #no se ejecuta la linea
    else:
        return 3 * 2
    
    def factorial_recursivo(2):
        if 2 == 0: #2 == 0 -> False
            return 1 #no se ejecuta la linea
        else:
            return 2 * 1
        
def factorial_recursivo(1):
    if 1 == 0:
        return 1
    else:
        return 1 * 1
    
def factorial_recursivo(0):
    if 0 == 0: #0 == 0 -> True
        return 1 # se ejecuta la linea
    """else:
        return n * factorial_recursivo(n - 1)"""

def saludar_en_ingles():
    return "Hello, how are you?"

def saludar():
    return saludar_en_ingles()

print(saludar())