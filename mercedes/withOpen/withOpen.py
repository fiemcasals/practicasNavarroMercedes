
#metodos w -> write. genera un archivo o pisa uno viejo bajo el mismo nombre
#metodo a -> append -> agregar informacion ala ya existente
# metodo r -> se usa para leer.
#la extencion .txt .odt .docx .pdf .csv .xlsx .json .xml .html son extensiones de archivos de texto, cada una con un formato diferente.
file = open("texto.txt", "w") #el primero es el nombre del archivo y el segundo el modo: lectura 'r' o escritura si no existe 'w', si existe borra lo anterior y lo reescribe, el metodo a hace referencia a append y lo que hace es guardar al final la nueva informacion.

file.write("hola, este es mi archivo de prueba llamado texto.txt\nComo vieron el salto de linea es igual que cuando uso print")
file.write("esto es otra linea")

print(file.closed)#esto nos dice si el archivo esta abierto o cerrado


file.close() #esto cierra el archivo, si no lo hacemos, el archivo queda abierto y no se pueden hacer mas operaciones con el.

print(file.closed)

