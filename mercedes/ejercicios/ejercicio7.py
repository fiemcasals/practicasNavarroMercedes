"""7. Se  necesita  una  función  que reciba  un  texto  de  varias  palabras separadas  por un  espacio,  con  letras 
mayúsculas  y  minúsculas,  y  retorne  una  colección  las  palabras  utilizadas,  todas  en  minúscula  y  sin duplicados 
 
Resultado Esperado: Si por ejemplo el programa solicitara ingresar el texto y el usuario ingresa: 
Por favor, ingrese un texto: HOLA NO Deberia deberia haber duplicados de de 
de de de ningun tipo 
 
 Se debería obtener como resultado: {'haber', 'ningun', 'duplicados', 'deberia', 
'tipo', 'no', 'de', 'hola'}"""



def palabras_unicas(texto):
    # Convertir todo a minúsculas
    texto = texto.lower()
    # Separar en palabras
    palabras = texto.split() #texto.split(",") #puedo variar el separador
    # Crear un conjunto (set) para eliminar duplicados automáticamente
    return set(palabras)

# Ejemplo de uso
entrada = input("Por favor, ingrese un texto: ")
resultado = palabras_unicas(entrada)
print(resultado)
