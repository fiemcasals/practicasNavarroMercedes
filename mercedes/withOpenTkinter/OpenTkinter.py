import tkinter as tk  # Importamos Tkinter para crear la interfaz gráfica
from tkinter import messagebox  # Para mostrar ventanas emergentes
#no deberia ser necesario importarlo nuevamente, mas bien llamar a tk.messagebox.showinfo
import os  # Para manejar rutas de archivos
import csv  # Para escribir en archivos .csv

# --- Determinar la carpeta del script actual
script_dir = os.path.dirname(os.path.abspath(__file__))

# --- Definir ruta al archivo CSV donde se guarda la planilla general
archivo_csv = os.path.join(script_dir, "planilla.csv")

# --- Si el archivo CSV no existe, lo creamos y escribimos los encabezados
if not os.path.exists(archivo_csv):
    with open(archivo_csv, "w", newline='') as f: #evita saltos de linea por defecto en write
        writer = csv.writer(f)
        writer.writerow(["Nombre", "Apellido", "Edad", "Email", "DNI"])  # Encabezados de columnas
        #writer.writerows(lista_de_vectores) #copia varias filas a la vez, cada fila es un vector

# --- Función que se ejecuta al presionar el botón "Guardar alumno"
def guardar():
    # Obtener el contenido de cada campo de entrada
    nombre = entry_nombre.get()
    apellido = entry_apellido.get()
    edad = entry_edad.get()
    email = entry_email.get()
    dni = entry_dni.get()

    # Validar que todos los campos estén completos
    if not (nombre and apellido and edad and email and dni):
        messagebox.showwarning("Faltan datos", "Por favor, completá todos los campos.")
        return  # Se corta la función si falta algo

    # --- Guardar los datos en la planilla general CSV
    with open(archivo_csv, "a", newline='') as f:#modo "a" appendea. es decir no borra lo anterior en el caso de existir, sino que continua escribiendo, si no existe, lo crea
        writer = csv.writer(f)
        writer.writerow([nombre, apellido, edad, email, dni])  # Escribimos los datos del alumno

    # --- Crear un archivo de texto individual con una "clave" derivada del nombre y apellido
    clave = (nombre + "_" + apellido + "_" + dni).lower().replace(" ", "")  # Generamos una clave única
    #con replace si hay un espacio vacio lo cambia por nada, es decir lo elimina
    archivo_individual = os.path.join(script_dir, f"{clave}.txt")  # Ruta del nuevo archivo .txt

    # Escribimos los mismos datos en ese archivo individual
    with open(archivo_individual, "w") as f:
        f.write(f"Nombre: {nombre}\n")
        f.write(f"Apellido: {apellido}\n")
        f.write(f"Edad: {edad}\n")
        f.write(f"Email: {email}\n")
        f.write(f"DNI: {dni}\n")

    # Mostrar mensaje de éxito
    messagebox.showinfo("Guardado", f"Alumno guardado correctamente.\nArchivo generado: {clave}.txt")

    # Limpiar los campos del formulario
    for entry in (entry_nombre, entry_apellido, entry_edad, entry_email, entry_dni):#recorre la tupla de objetos y los limpia
        entry.delete(0, tk.END)#el 0 indica que desde el primer caracter, y el tk.END indica que hasta el final del campo, es decir hasta el ultimo caracter debe borrar

# --- Crear la ventana principal
ventana = tk.Tk()
ventana.title("Registro de Alumnos")  # Título de la ventana

# --- Crear y ubicar etiquetas de cada campo
tk.Label(ventana, text="Nombre").grid(row=0, column=0)
tk.Label(ventana, text="Apellido").grid(row=1, column=0)
tk.Label(ventana, text="Edad").grid(row=2, column=0)
tk.Label(ventana, text="Email").grid(row=3, column=0)
tk.Label(ventana, text="DNI").grid(row=4, column=0)

"""# --- Crear y ubicar etiquetas de cada campo usando un for
etiquetas = ["Nombre", "Apellido", "Edad", "Email", "DNI"]
for i, texto in enumerate(etiquetas):
    tk.Label(ventana, text=texto).grid(row=i, column=0)
"""

# --- Crear campos de entrada
entry_nombre = tk.Entry(ventana)
entry_apellido = tk.Entry(ventana)
entry_edad = tk.Entry(ventana)
entry_email = tk.Entry(ventana)
entry_dni = tk.Entry(ventana)

# --- Ubicar los campos en la interfaz
entry_nombre.grid(row=0, column=1)
entry_apellido.grid(row=1, column=1)
entry_edad.grid(row=2, column=1)
entry_email.grid(row=3, column=1)
entry_dni.grid(row=4, column=1)

"""# --- Crear y ubicar campos de entrada con un for
entries = []
for i in range(5):
    entry = tk.Entry(ventana)
    entry.grid(row=i, column=1)
    entries.append(entry)

# Asignar cada campo a su variable correspondiente (opcional pero útil)
entry_nombre, entry_apellido, entry_edad, entry_email, entry_dni = entries
"""
# --- Botón para guardar los datos ingresados
tk.Button(ventana, text="Guardar alumno", command=guardar).grid(row=5, column=0, columnspan=2, pady=10)
#guardar no lleva parentesis como estamos acostumbrados, pq debe esperar que aprieten el boton
#columnspan=2 le dice que el boton debe ocupar dos columnas de ancho
#pady=10 deja espacio de 10 pixeles arriba y abajo
# --- Iniciar el bucle principal de la interfaz


#para probar
#ventana.columnconfigure(0, minsize=100)  # Columna 0: ancho mínimo 100px
#ventana.rowconfigure(2, minsize=50)  # Fila 2: alto mínimo 50px

#También podés usar weight para que una columna se expanda proporcionalmente cuando redimensionás la ventana:
#ventana.columnconfigure(1, weight=1)

#entry = tk.Entry(ventana, width=30)  # 30 caracteres de ancho (no píxeles)


ventana.mainloop()# Inicia el bucle principal de la interfaz