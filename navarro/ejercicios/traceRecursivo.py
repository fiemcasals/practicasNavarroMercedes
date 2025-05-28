def resultado_suma_lista(lista, nivel=0):
    """
    Suma todos los elementos de una lista de forma recursiva.
    Muestra el proceso de llamada y retorno.
    """
    indent = "  " * nivel  # sangría para mostrar el nivel de recursión
    print(f"{indent}Llamando con lista: {lista}")

    if not lista:
        print(f"{indent}Lista vacía, retorno 0")
        return 0

    primer_valor = lista[0]
    resto = lista[1:]

    print(f"{indent}Primer valor: {primer_valor}, resto: {resto}")

    suma_resto = resultado_suma_lista(resto, nivel + 1)

    total = primer_valor + suma_resto
    print(f"{indent}Retornando: {primer_valor} + {suma_resto} = {total}")
    return total


print("Resultado final:", resultado_suma_lista([1, 2, 3, 4]))



