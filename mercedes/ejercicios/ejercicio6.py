"""6. Se necesita un programa que reciba por línea de comando una serie de palabras, hasta que reciba la 
palabra "exit". Una vez recibida dicha instrucción, debe mostrar por salida standard las mismas palabras 
ingresadas,  almacenadas  en  una  lista,  pero  ordenadas  alfabéticamente  y  cada  una  debe  estar 
capitalizada.  
 
Resultado Esperado: El programa le solicita al usuario que ingrese y este escribe: 
Ingrese palabra: hola 
Ingrese palabra: QUE 
Ingrese palabra: tal 
Ingrese palabra: como 
Ingrese palabra: estas 
Ingrese palabra: exit 
 
Se espera recibir el siguiente resultado: ['Como', 'Estas', 'Hola', 'Que', 'Tal']"""

def main():
    palabras = []

    while True:
        entrada = input("Ingrese palabra: ")
        if entrada.lower() == "exit":
            break
        palabras.append(entrada.capitalize())#se asegura que la primera letra sea mayuscula

    palabras.sort()#ordena las plabras alfabeticamente como un diccionario
    print(palabras)

# Ejecutar el programa
if __name__ == "__main__":
    main()