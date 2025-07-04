import re
import os

# Ruta del archivo que queremos leer
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "saludos.py") 

# Lista para guardar los nombres encontrados
nombres = []

# Leer el archivo línea por línea
with open(file_path, "r", encoding="utf-8") as f:
    for linea in f:
        # Buscar coincidencias con print("Hola, Nombre")
        coincidencia = re.search(r'print\("Hola, (\w+)"\)', linea)
        if coincidencia:
            nombres.append(coincidencia.group(1))  # Guardamos el nombre

# Mostrar los nombres encontrados
print("Nombres saludados:")
for nombre in nombres:
    print("-", nombre)
