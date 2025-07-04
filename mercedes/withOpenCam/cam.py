import tkinter as tk
from tkinter import messagebox 
import os
import csv
import cv2
import pytesseract
import datetime
import re

# Obtener la ruta del directorio actual donde se encuentra este script
script_dir = os.path.dirname(os.path.abspath(__file__))
archivo_csv = os.path.join(script_dir, "planilla.csv")  # Ruta del archivo CSV general

# Si el archivo CSV no existe, crearlo con encabezados
if not os.path.exists(archivo_csv):
    with open(archivo_csv, "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Nombre", "Apellido", "Edad", "Email", "DNI"])

# Función que guarda los datos del formulario en el archivo CSV y en un .txt
def guardar():
    nombre = entry_nombre.get()
    apellido = entry_apellido.get()
    edad = entry_edad.get()
    email = entry_email.get()
    dni = entry_dni.get()

    if not (nombre and apellido and edad and email and dni):
        messagebox.showwarning("Faltan datos", "Por favor, completá todos los campos.")
        return

    with open(archivo_csv, "a", newline='') as f:
        writer = csv.writer(f)
        writer.writerow([nombre, apellido, edad, email, dni])

    clave = (nombre + "_" + apellido).lower().replace(" ", "")
    archivo_txt = os.path.join(script_dir, f"{clave}.txt")
    with open(archivo_txt, "w") as f:
        f.write(f"Nombre: {nombre}\nApellido: {apellido}\nEdad: {edad}\nEmail: {email}\nDNI: {dni}\n")

    messagebox.showinfo("Guardado", f"Alumno guardado y archivo {clave}.txt creado.")
    for entry in (entry_nombre, entry_apellido, entry_edad, entry_email, entry_dni):
        entry.delete(0, tk.END)

# Función que carga la imagen 'foto_dni.jpg', aplica OCR y completa los campos
def escanear_dni():
    ruta_imagen = os.path.join(script_dir, "foto_dni.jpg")
    if not os.path.exists(ruta_imagen):
        messagebox.showerror("Error", "No se encontró la imagen 'foto_dni.jpg' en el directorio del script.")
        return

    img = cv2.imread(ruta_imagen)
    texto = pytesseract.image_to_string(img)
    print("Texto detectado por OCR:\n", texto)

    texto_sin_puntos = texto.replace(".", "")
    lineas = texto_sin_puntos.split("\n")
    lineas = [l.strip() for l in lineas if l.strip()]#el condicional filtra las lineas vacias, ya que stip elimina espacios al principio y al final de cada linea

    apellido_detectado = ""
    nombre_detectado = ""
    for i, linea in enumerate(lineas):
        if "apellido" in linea.lower() and i + 1 < len(lineas):
            apellido_detectado = lineas[i + 1].strip().title()#Convierte el texto a formato "Título", es decir, pone en mayúscula la primera letra de cada palabra y el resto en minúscula
        if "nombre" in linea.lower() and i + 1 < len(lineas):
            nombre_detectado = lineas[i + 1].strip().title().lstrip('_')#elimina '_' #la l es de left, existe sin prefijo o con r de rigth

    if apellido_detectado:
        entry_apellido.delete(0, tk.END)
        entry_apellido.insert(0, apellido_detectado)
        print(f"Apellido insertado: {apellido_detectado}")
    if nombre_detectado:
        entry_nombre.delete(0, tk.END)
        entry_nombre.insert(0, nombre_detectado)
        print(f"Nombre insertado: {nombre_detectado}")

    # Buscar número de DNI (7 u 8 dígitos seguidos)
    dni_match = re.search(r'\b(\d{7,8})\b', texto_sin_puntos)#busca digitos de 7 u 8 caracteres.
    if dni_match:
        entry_dni.delete(0, tk.END)
        entry_dni.insert(0, dni_match.group(1))#con los parentecis en la linea 78 hacemos grupos de busqueda, en este caso hay un solo grupo.
        print("DNI insertado:", dni_match.group(1))

   # Buscar fecha de nacimiento con OCR tolerante a errores
    fecha_match = re.search(r'(\d{1,2})\D+(ene|feb|mar|abr|may|jun|jul|ago|sep|oct|nov|dic)[a-z]*\D+(\d{4})', texto.lower())

    if fecha_match:
        dia, mes_str, anio = fecha_match.groups()
        try:
            # Diccionario más robusto
            meses = {
                "ene": 1, "enero": 1,
                "feb": 2, "febrero": 2,
                "mar": 3, "marzo": 3,
                "abr": 4, "abril": 4,
                "may": 5, "mayo": 5,
                "jun": 6, "junio": 6,
                "jul": 7, "julio": 7,
                "ago": 8, "agosto": 8,
                "sep": 9, "sept": 9, "septiembre": 9,
                "oct": 10, "octubre": 10,
                "nov": 11, "noviembre": 11,
                "dic": 12, "diciembre": 12
            }

            mes_key = mes_str.lower()[:3]  # Tomamos solo los primeros 3 caracteres
            mes = meses.get(mes_key, 0)
            if mes:
                fecha_nac = datetime.datetime(int(anio), mes, int(dia))
                hoy = datetime.datetime.now()
                edad = hoy.year - fecha_nac.year - ((hoy.month, hoy.day) < (fecha_nac.month, fecha_nac.day))
                entry_edad.delete(0, tk.END)
                entry_edad.insert(0, str(edad))
                print("Edad calculada:", edad)
            else:
                print("Mes no reconocido:", mes_str)
        except Exception as e:
            print("Error al calcular edad:", e)


        messagebox.showinfo("OCR", "Texto procesado. Verificá los campos completados.")

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Registro de Alumnos con OCR")

# Etiquetas de los campos
tk.Label(ventana, text="Nombre").grid(row=0, column=0)
tk.Label(ventana, text="Apellido").grid(row=1, column=0)
tk.Label(ventana, text="Edad").grid(row=2, column=0)
tk.Label(ventana, text="Email").grid(row=3, column=0)
tk.Label(ventana, text="DNI").grid(row=4, column=0)

# Campos de entrada de texto
entry_nombre = tk.Entry(ventana)
entry_apellido = tk.Entry(ventana)
entry_edad = tk.Entry(ventana)
entry_email = tk.Entry(ventana)
entry_dni = tk.Entry(ventana)

entry_nombre.grid(row=0, column=1)
entry_apellido.grid(row=1, column=1)
entry_edad.grid(row=2, column=1)
entry_email.grid(row=3, column=1)
entry_dni.grid(row=4, column=1)

# Botones
tk.Button(ventana, text="Guardar alumno", command=guardar).grid(row=5, column=0, columnspan=2, pady=10)
tk.Button(ventana, text="Escanear DNI", command=escanear_dni).grid(row=6, column=0, columnspan=2, pady=5)

ventana.mainloop()
