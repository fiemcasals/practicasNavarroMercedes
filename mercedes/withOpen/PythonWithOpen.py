import os  # Importamos el módulo 'os' que nos permite interactuar con el sistema operativo (como rutas de archivos)

# Obtenemos la ruta completa del archivo actual (el script .py)
# __file__ es una variable especial de cada script de python que contiene el nombre del archivo actual. ej: withOpenPath.py
# os.path.abspath(__file__) convierte eso en una ruta absoluta (completa). ej: /home/mauri/uni/proyecto/withOpen/withOpen.py
# os.path.dirname(...) extrae solo la carpeta que contiene el script. ej: /home/mauri/uni/proyecto/withOpen
script_dir = os.path.dirname(os.path.abspath(__file__))
#script_dir = "/home/mauri"
#relativePath = withOpen/withOpenPath.py
#absolutePath = /home/mauri/uni/UTN/temasDadosClasesUTN/practicasUTN/mercedes/withOpen/withOpenPath.py
# Creamos una ruta al archivo 'texto.txt' dentro de esa misma carpeta
# Esto garantiza que el archivo se cree "al lado del script", sin importar desde dónde se ejecute
file_path = os.path.join(script_dir, "codigoGenerado.py") #ej: "/home/mauri/uni/UTN/withOpen/texto.txt"


# Abrimos (o creamos) el archivo en modo escritura ("w") usando la ruta completa
# El bloque 'with' asegura que el archivo se cierre correctamente después de escribir
with open(file_path, "w") as file:
    # Escribimos la primera línea y agregamos un salto de línea (\n) al final
    file.write("print('hola mundo')")

   
# Imprimimos la ruta donde se guardó el archivo, como confirmación
print(f"Archivo creado en: {file_path}")
