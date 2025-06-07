class Calculadora:
    def sumar(self, a, b):
        return a + b

    def restar(self, a, b):
        return a - b

    def multiplicar(self, a, b):
        return a * b

    def dividir(self, a, b):
        if b == 0:
            return "Error: No se puede dividir por cero"
        return a / b


def main():
    calc = Calculadora() 
    
    while True:
        print("\n--- Calculadora Básica ---")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Salir")

        opcion = input("Elegí una opción (1-5): ")

        if opcion == "5":
            print("Saliendo de la calculadora. ¡Hasta luego!")
            break  # finaliza el bucle

        if opcion not in ["1", "2", "3", "4"]:
            print("Opción inválida. Intentalo de nuevo.")
            continue  # vuelve al inicio del bucle

        try:
            num1 = float(input("Ingresá el primer número: "))
            num2 = float(input("Ingresá el segundo número: "))
        except ValueError:
            print("Entrada inválida. Solo se aceptan números.")
            continue

        if opcion == "1":
            resultado = calc.sumar(num1, num2)
        elif opcion == "2":
            resultado = calc.restar(num1, num2)
        elif opcion == "3":
            resultado = calc.multiplicar(num1, num2)
        elif opcion == "4":
            resultado = calc.dividir(num1, num2)

        print(f"El resultado es: {resultado}")


# Ejecutar el programa
if __name__ == "__main__":
    main()
