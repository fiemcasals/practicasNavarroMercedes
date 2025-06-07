"""b. Modificar la función anterior, pero obteniendo correctamente cada dato según su tipo (numero entero, 
string o boolean). Se considera que el string siempre tiene la forma de primer campo un entero, luego un 
texto y por ultimo un boolean. 
 
Resultado Esperado: Si se envia '14,Juana Perez,True' se espera que la función retorne la 
lista [14, 'Juana Perez', True]"""

"""c. Utilizando la función realizada en el punto 4b, hace una nueva función que reciba una  lista de strings y 
retorna otra lista, como listas con los campos formateados (mantener el mismo formato de string que el 
punto b, es decir, entero, texto y boolean).  
 
Resultado Esperado: Si se envía la siguiente lista como parámetro de la función: 
 
[  
    '14,Juana Perez,True',  
    '16,Raul Dell,False',  
    '18,Mariana Castillo,True',  
    '176,Pedro Rodríguez,False' 
   ] 
 
Se espera obtener la lista: 
 [[14, 'Juana Perez', True], [16, 'Raul Dell', True], [18, 'Mariana Castillo', 
True], [176, 'Pedro Rodríguez', True]]"""

def parse_string(data_str):
    """Convierte un string 'entero,texto,boolean' en una lista con tipos apropiados."""
    parts = data_str.split(',')
    return [int(parts[0]), parts[1], parts[2].strip().lower() == 'true']

def parse_list_of_strings(string_list):
    """Convierte una lista de strings con formato 'entero,texto,boolean' en listas con tipos apropiados."""
    return [parse_string(s) for s in string_list]

datos = [
    '14,Juana Perez,True',
    '16,Raul Dell,True',
    '18,Mariana Castillo,True',
    '176,Pedro Rodríguez,True'
]

resultado = parse_list_of_strings(datos)
print(resultado)


#verificar si "variable" es un digito con isdigit
def is_digit(variable):
    return variable.isdigit()

#verificar si "variable" es un booleano"
def is_boolean(variable):
    return isinstance(variable, bool)


for lista in resultado:
    print(f" el primer elemento {lista[0]} es un digito? {is_digit(str(lista[0]))}")
    print(f" el segundo elemento {lista[1]} es un string? {isinstance(lista[1], str)}")
    print(f" el tercer elemento {lista[2]} es un booleano? {is_boolean(lista[2])}")


def is_palindrome(word):
    """Verifica si una palabra es un palíndromo."""
    word = word.lower().replace(" ", "")  # Ignorar mayúsculas y espacios
    return word == word[::-1]

# Ejemplo de uso
palabra = "radar"
print(f"¿La palabra '{palabra}' es un palíndromo? {is_palindrome(palabra)}")