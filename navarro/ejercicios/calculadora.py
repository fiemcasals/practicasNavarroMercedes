import operator

class Calculadora:
    def __init__(self):
        self.operaciones = operator.

        self.diccionarioOperaciones = {1:operator.add,2:operator.sub,3:operator.le}

    def operacionesDisponibles(self):
        return self.operaciones

    def sumar(self, primerValor, segundoValor):
        resultado = primerValor + segundoValor
        return resultado
    
    def restar(self,primerValor, segundoValor):
        return primerValor - segundoValor
    
    def multiplicacion(self, primerValor, segundoValor):
        return primerValor * segundoValor
    
    def division(self, primerValor, segundoValor):
        return primerValor / segundoValor
    
    def divisionEx (self, primerValor, segundoValor):
        return primerValor // segundoValor
    
    def menu(self):
        print("Menu de opciones:")
        print("ingrese 1 para sumar")
        print("ingrese 2 para restar")

        return int(input())
    
    def __str__(self):
        print("las operaciones son todas las de operator")

calc = Calculadora()

"""primerValor = int(input("ingrese el primer valor"))
segundoValor = int(input("ingrese el segundo valor"))
indice_del_diccionario_de_operaciones = calc.menu()
tipo_de_operacion_a_realizar = calc.diccionarioOperaciones[indice_del_diccionario_de_operaciones]
resultado = tipo_de_operacion_a_realizar(primerValor, segundoValor )

print (resultado)"""



print(calc.operacionesDisponibles())

print(calc.diccionarioOperaciones[calc.menu()](int(input("primer valor")), int(input("segundo valor"))