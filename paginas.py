#editar paginas

import os

def replace_text(file_path, old_text, new_text):
    with open(file_path, 'r', encoding="utf8") as file:
        content = file.read()
        
    # Reemplazar el texto antiguo por el nuevo
    content = content.replace(old_text, new_text, 1)
    
    # Escribir el contenido modificado de vuelta al archivo
    with open(file_path, 'w', encoding="utf8") as file:
        file.write(content)

    print("yata")
        
# Uso de la función
# (Asegúrate de que 'your_file.txt' existe o usa tu propio archivo)
#file_path = 'C:/Users/Isaac/Desktop/SaaS/indexer/blog/Abogados/Diseño-Páginas-Web-Abogados-Albacete.mdx'  
old_text = '.webp'  # Texto que deseas reemplazar
new_text = ''

#replace_text(file_path, old_text, new_text)


def get_file_paths(root_folder):
    file_paths = []

    for folder, _, files in os.walk(root_folder):
        for file in files:
            file_paths.append(os.path.join(folder, file))
            
    return file_paths

# Uso de la función
# (Asegúrate de que 'root_folder' es el path correcto para tu uso caso)
root_folder = '/home/faiya/proyects/astro-blog-template/src/content/blog'
file_paths = get_file_paths(root_folder)

n=0

# Imprimir las rutas de los archivos y/o guardarlos según tu necesidad
for path in file_paths:
    n=n+1
    print(n)
    print(path)
    replace_text(path, old_text, new_text)