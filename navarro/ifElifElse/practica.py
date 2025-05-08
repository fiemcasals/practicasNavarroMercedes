"""#voy a mostrar el uso concatenado de if, elif y por ultimo else

ingreso = 30000

coeficiente = 0.5

if ingreso > 10000:
    print("ingreso es mayor a 10000")
#yo quiero materializar que ingreso es menor a 10000 y a la vez mayor a 20000
elif ingreso > 2000:
    print("ingreso es mayor a 2000 y menor a 10000")
else:
    print("ingreso es menor a 2000")
    """
"""
#voy a evaluar el valor real del coeficiente segun mi ingreso
if ingreso > 10000:
    coeficiente = 0.75
elif ingreso > 2000:
    coeficiente = 0.5
else:
    coeficiente = 0.25"""

"""print(" usted va a pagar su ingreso por el coeficiente es decir: ", coeficiente * ingreso)

#es un ejemplo donde ingreso mi edad y el sistema me dice si soy adulto o que soy
edad = int(input("ingrese su edad: "))"""

"""
if edad < 12:
    print("sos un niño")
elif edad < 18:
    print("no es un ninio")
elif edad < 30:
    print("sos un joven")
else:
    print("sos un adulto")"""


"""
salario = int(input("ingrese su salario: "))
print(salario)"""
   
"""

ingresos = 20000
coeficiente = 0.1 if ingresos > 30000 else 0.5
print("El coeficiente es:", coeficiente)"""

"""ingresos = 40000
coeficiente = (0.15, 0.1)[ingresos > 30000] #-> f or v

print("El coeficiente es:", coeficiente)

#quiero cargar el coeficiente segun el ingreso con condicionales if en una sola linea
coeficiente = 0.15 if ingresos > 30000 else 0.1"""

numero = int(input("ingrese un numero: "))
tipo = "par" if numero % 2 == 0 else "impar"
#imprimir el tipo de dato
print("El numero es:", tipo)