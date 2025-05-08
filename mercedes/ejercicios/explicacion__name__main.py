
#yo importo el archivo ejercicio2bisPracticaAlumnos.py que se encuentra en la misma carpeta
import ejercicio2bisPracticaAlumnos as ej2

# corro este archivo para ver si funciona

if __name__ == "__main__":
    #quiero ver si auto es un palindromo
    print(f" este print pertenece a la explicacion de name__main: {ej2.es_palindromo("auto")}") # False


#ahora edito el archivo ejercicio2bisPracticaAlumnos.py para ver si se ejecutan todas las pruebas, borrando el condicional if __name__ == "__main__":

#cambie el if __name__ == "__main__": por if True: para que se ejecute todo el archivo