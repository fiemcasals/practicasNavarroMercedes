
def condicional(numero):

    if numero > 50:
        respuesta = f"el numero {numero} es mayor a 50"
    elif numero <20:
        respuesta = f"el numero {numero} es menor a 20"
    else:
        respuesta = "no coincide con ningun condicional"
    return respuesta

print(condicional(int(input("ingrese un numero entre el 0 y el 100: "))))
print("terminaste")