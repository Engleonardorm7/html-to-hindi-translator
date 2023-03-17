

# Define el directorio base donde se encuentran los archivos HTML

import os
import glob
from bs4 import BeautifulSoup
from mtranslate import translate

# Define el directorio base donde se encuentran los archivos HTML
base_dir = './pagina traducida/www.classcentral.com'

# Define la ruta de la carpeta donde se guardarán los archivos traducidos
output_dir = './prueba de archivos a traducir'

# Itera sobre todos los archivos y subdirectorios en el directorio base
for root, dirs, files in os.walk(base_dir):
    for file in files:
        # Filtra aquellos archivos cuyo nombre sea "index.html"
        # if file == 'index.html':
        if file.endswith('.html') and os.path.dirname(root) != os.path.join(base_dir, 'report'):
            # Crea la ruta completa del archivo
            file_path = os.path.join(root, file)
            print(f'Procesando archivo: {file_path}')
            
            # Aplica el programa anterior al archivo
            # with open(file_path, 'r', encoding='utf-8') as f:
            #     html = f.read()
            
            # soup = BeautifulSoup(html, 'html.parser')
            # # ... realiza la traducción del archivo con el programa
            print("starting")
            # Leer el archivo HTML
            with open (file_path, 'r', encoding='utf-8') as f:
                print("reading")
                html = f.read()

            # Crear un objeto BeautifulSoup para analizar el HTML
            soup = BeautifulSoup(html, 'html.parser')
            print("searching")


            # Buscar todos los elementos h1, h2, p, a, li, span, y div que contienen texto
            text_elements = soup.find_all(['h1', 'h2', 'p',{'class': 'text-2'}, 'a', 'li', 'span', 'div', {'class': 'wysiwyg text-1'},'b','em','td','strong','section','header','footer','i','ul','button','href','time','figcaption'], text=True)

            # Extraer el texto de cada elemento y agregarlo a una lista
            # text_list = []
            # for element in text_elements:
            #     text = element.get_text(strip=True)
            #     if text:
            #         text_list.append(text)

            print("translating")
            for element in text_elements:
                try:
                    text = element.string
                    #print(text)

                    translated_text = translate(str(text), 'hi')
                    print(f'{text} - {translated_text}')
                    element.string.replace_with(translated_text)
                except:
                    pass

            print("writing")
            # Escribir el contenido modificado en un nuevo archivo HTML
            
            # Crea una carpeta con el mismo nombre que el archivo original dentro de output_dir
            output_path = os.path.join(output_dir, os.path.basename(root), file)
            os.makedirs(os.path.dirname(output_path), exist_ok=True)
            
            # Escribe el archivo traducido dentro de la carpeta creada
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(str(soup))
            print("done")