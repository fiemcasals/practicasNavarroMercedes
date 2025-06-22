from deep_translator import GoogleTranslator
import re

def cargar_oraciones(ruta_archivo):
    with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
        texto = archivo.read()
    
    # Dividimos el texto en oraciones usando puntos, signos de exclamación o pregunta
    oraciones = re.split(r'(?<=[.!?]) +', texto)
    return oraciones

def mostrar_oraciones(oraciones):
    traductor = GoogleTranslator(source='en', target='es')
    for oracion in oraciones:
        print(f"\n📝 Oración: {oracion}")
        input("👉 Presioná Enter para ver la traducción...")
        try:
            traduccion = traductor.translate(oracion)
        except Exception as e:
            traduccion = f"(Error al traducir: {e})"
        print(f"🔁 Traducción: {traduccion}")
        input("👉 Presioná Enter para continuar...")

def main():
    archivo = input("📄 Ingresá la ubicacion del archivo")
    try:
        oraciones = cargar_oraciones(archivo)
        mostrar_oraciones(oraciones)
    except FileNotFoundError:
        print("❌ Archivo no encontrado.")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()
