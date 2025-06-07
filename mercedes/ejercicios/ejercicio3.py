def generar_diccionario_ascii():
    diccionario = {}
    for letra in range(ord('a'), ord('z') + 1):
        diccionario[chr(letra)] = letra
    return diccionario

# Ejemplo de uso
print(generar_diccionario_ascii())


print(ord('a'))  # 97
print(chr(97))  # 'a'





