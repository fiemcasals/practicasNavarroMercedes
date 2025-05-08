import operator

a = 10
b = 3


#suma -> operator.add
suma = operator.add(a,b)
print(f"Suma: {suma}")


#resta -> operator.sub
resta = operator.sub(a,b)
print(f"Resta: {resta}")

#multiplicacion -> operator.mul
multiplicacion = operator.mul(a,b)
print(f"Multiplicacion: {multiplicacion}")

#division -> operator.truediv
division = operator.truediv(a,b) 
print(f"Division: {division}")

#division entera -> operator.floordiv
division_entera = operator.floordiv(a,b)
print(f"Division entera: {division_entera}")

#potencia -> operator.pow
potencia = operator.pow(a,b)
print(f"Potencia: {potencia}")

#modulo -> operator.mod
modulo = operator.mod(a,b)
print(f"Modulo: {modulo}")

#comparacion -> operator.eq
comparacion = operator.eq(a,b)
print(f"Comparacion: {comparacion}")

#comparacion -> operator.ne
comparacion = operator.ne(a,b)
print(f"Comparacion: {comparacion}")




"""@fiemcasals ➜ /workspaces/languages (insertarOrdenado) $ /home/codespace/.python/current/bin/python3 /workspaces/languages/temas/operadores/operator.py
Traceback (most recent call last):
  File "/workspaces/languages/temas/operadores/operator.py", line 1, in <module>
    import operator  # Importamos todo el módulo operator
    ^^^^^^^^^^^^^^^
  File "/workspaces/languages/temas/operadores/operator.py", line 8, in <module>
    resultado_suma = operator.add(a, b)
                     ^^^^^^^^^^^^
AttributeError: partially initialized module 'operator' has no attribute 'add' (most likely due to a circular import)"""
