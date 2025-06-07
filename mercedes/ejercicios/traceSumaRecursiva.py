"""python -m trace --trace mi_script.py
"""
#yo lo llame traceSumaRecursiva.py

# mi_script.py 

def resultado_suma_lista(lista):
    """
    Suma todos los elementos de una lista de forma recursiva.
    """
    if not lista:
        return 0
    return lista[0] + resultado_suma_lista(lista[1:])

print(resultado_suma_lista([1, 2, 3, 4]))
