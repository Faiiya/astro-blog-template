import os

# Ruta de la carpeta que contiene los archivos .mdx
carpeta = '/ruta/de/tu/carpeta'

# Itera sobre cada archivo en la carpeta
for nombre_archivo in os.listdir(carpeta):
    # Verifica si el archivo es de tipo .mdx
    if nombre_archivo.endswith(".mdx"):
        # Construye la ruta completa del archivo
        ruta_completa = os.path.join(carpeta, nombre_archivo)

        # Lee el contenido del archivo
        with open(ruta_completa, 'r', encoding='utf-8') as archivo:
            contenido = archivo.read()

        # Reemplaza ".webp" con "" en el contenido
        nuevo_contenido = contenido.replace(".webp", "")

        # Escribe el nuevo contenido de vuelta al archivo
        with open(ruta_completa, 'w', encoding='utf-8') as archivo:
            archivo.write(nuevo_contenido)

print("Proceso completado.")