
coeficiente = 0.05 #valor por defecto

sueldo = 20000




if sueldo < 30000:
    coeficiente = 0.1
elif sueldo < 20000:
    coeficiente = 0.07
elif sueldo < 10000:
    coeficiente = 0.03
elif sueldo < 5000:
    coeficiente = 0.01
else: #es el fragmento de codigo por defecto
    coeficiente = 0.05

print("Lo que debe pagar es:", coeficiente * sueldo)


ingreso = float (input("Ingrese su ingreso: "))

#cargo el nombre 
nombre = input("Ingrese su nombre: ")

#imprimo el nombre con el ingreso
print("Hola", nombre, "tus ingresos son:", ingreso)


coeficiente = 0.1 if ingreso < 30000 else 0.05

coeficiente = (0.15, 0.1) [ingreso < 30000] #si ingreso es menor a 30000, coeficiente = 0.15, sino 0.1


tipo = "par" if ingreso % 2 == 0: