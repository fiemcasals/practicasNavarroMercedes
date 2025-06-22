class Operador:
    def __init__(self):
        pass

    def operar(self, string, palabra):
        return string.split(palabra)
    
    def operarMatriz(self, matriz, caracter):
        resultado = []
        vector = []
        for fila in matriz:
            vector = fila[0].split(caracter)
            for palabra in vector:
                resultado.append(palabra)
        return resultado
    
operador = Operador()

matriz = [["hola,estas,todo,bien"], ["bien, y , vos"]]

print(operador.operarMatriz(matriz, ","))




#"hola * todo * bien* ?"

#llamo a un metodo de una clase y le paso el string y el caracter que separa.

#me devuelve un vector separado por comas en donde hay un *.
#ej [hola,todo,bien,?]

#string.split("*").



[
    ["hola * estas * todo * bien"],
    ["bien *y*  vos"]
    ]

["hola", "estas", "todo", "bien", "bien", "y", "vos"]