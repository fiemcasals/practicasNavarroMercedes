nombres = ["Ana", "Luis", "María", "Javier", "Lucía"]
archivo_salida = "nombres_saludados.txt"
with open(archivo_salida, "w", encoding="utf-8") as f:
    for nombre in nombres:
        saludo = f"Hola, {nombre}! ¿Cómo estás?"
        print(saludo)           # Muestra el saludo por pantalla
        f.write(nombre + "\n")  # Guarda solo el nombre en el archivo
