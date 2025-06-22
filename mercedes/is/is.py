a = [1,2,3]
b = a # que esta copiando la direccion de memoria

print(a)
print(b)
print(a is b)


c = a.copy() #con este metodo no copio la direccion sino mas bien los valores alojados en a
print(c)
if a is c:
    print("las variable refieren a la misma posicion de memoria")
else:
    print("las variables se encuentran alojadas en distintas posiciones de memoria")


d = a[1:2]
print(d)