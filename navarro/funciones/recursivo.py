
def suma(valor_anterior):
    if valor_anterior == 5:
        print(f"llegaste al final")
    else:
        valor_anterior += 1
        print(valor_anterior)
        suma(valor_anterior)


suma(0)

