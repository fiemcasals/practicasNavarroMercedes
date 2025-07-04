import random

cant_ganada = 0 
cant_ganada_maq = 0

#funciones:
def elegir_opciones():
    condicion = True
    while condicion:
        opcion_usuario = input("ingrese piedra papel o tijera: ").lower().strip()
        if opcion_usuario in ["piedra", "papel", "tijera"]:
            condicion = False
        else:
            print("debe ingresar textualmente 'piedra', 'papel' o 'tijera'")
    opcion_maquina = random.choice(['piedra', 'papel', 'tijera'])

    print(f"la maquina eligio: {opcion_maquina}")
    return opcion_usuario, opcion_maquina

def determina_ganador(opcion_usuario, opcion_maquina):
    global cant_ganada
    global cant_ganada_maq

    if opcion_usuario == opcion_maquina:
        return "empate"
    #vamos a ver si ganaste:
    if opcion_usuario=='piedra' and opcion_maquina == 'tijeras' or opcion_usuario=='tijera' and opcion_maquina == 'papel' or opcion_usuario=='pepel' and opcion_maquina == 'piedra':
        cant_ganada = cant_ganada + 1 #cant_ganada +=1
        return "ganaste una ronda"
    cant_ganada_maq +=1   
    return "perdiste una ronda"
    
   
def main():

    while cant_ganada != 2 and cant_ganada_maq !=2:
        opcion_usuario, opcion_maquina = elegir_opciones()
        print(determina_ganador(opcion_usuario,opcion_maquina))

    if cant_ganada_maq == 2:
        print("perdiste el juego")
    else:
        print("ganaste el juego")


if __name__ == "__main__":
    main()