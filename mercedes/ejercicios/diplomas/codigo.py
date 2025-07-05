from PIL import Image, ImageDraw, ImageFont
import pandas as pd
import os


# --- Cargar los datos desde un CSV ---
datos = pd.read_csv("/home/mauri/uni/UTN/temasDadosClasesUTN/practicasUTN/mercedes/ejercicios/diplomas/datos.csv")  # Asegurate de tener este archivo en el mismo directorio

# --- Crear carpeta de salida si no existe ---
os.makedirs("diplomas_generados", exist_ok=True)

# --- Fuente (puede usar una fuente elegante tipo 'GreatVibes-Regular.ttf') ---
ruta_fuente = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

fuente_nombre = ImageFont.truetype(ruta_fuente, 40)
fuente_curso = ImageFont.truetype(ruta_fuente, 30)
fuente_fecha = ImageFont.truetype(ruta_fuente, 20)


# --- Recorrer cada fila del CSV y generar diploma ---
for index, fila in datos.iterrows():
    # Cargar imagen base
    imagen = Image.open("/home/mauri/uni/UTN/temasDadosClasesUTN/practicasUTN/mercedes/ejercicios/diplomas/diploma.png").convert("RGB")
    

    draw = ImageDraw.Draw(imagen)

    # --- Obtener datos ---
    nombre = fila["Nombre"]
    curso = fila["Curso"]
    fecha = fila["Fecha"]

   

# Abrir imagen base
imagen = Image.open("diploma.png").convert("RGB")
draw = ImageDraw.Draw(imagen)

# Usar fuente disponible (ajustá si tenés otra)
fuente_nombre = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 20)
fuente_curso = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 16)
fuente_fecha = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 12)

# Datos
nombre = "Juan Pérez"
curso = "Python Básico"
fecha = "Tucumán, 5 de Julio de 2025"

# --- Ubicar texto según el tamaño de imagen (457 x 337)
draw.text((130, 135), nombre, font=fuente_nombre, fill="black")   # A:
draw.text((70, 165), curso, font=fuente_curso, fill="black")      # motivo
draw.text((140, 200), fecha, font=fuente_fecha, fill="black")     # fecha

# Guardar resultado
imagen.save("diploma_generado.png")
