

import os
import glob
from bs4 import BeautifulSoup
from mtranslate import translate

base_dir = './pagina traducida/www.classcentral.com'


output_dir = './prueba de archivos a traducir'


for root, dirs, files in os.walk(base_dir):
    for file in files:
        
        if file.endswith('.html') and os.path.dirname(root) != os.path.join(base_dir, 'report'):
             
            file_path = os.path.join(root, file)
            print(f'Procesando archivo: {file_path}')
            
             
            print("starting")
             
            with open (file_path, 'r', encoding='utf-8') as f:
                print("reading")
                html = f.read()

             
            soup = BeautifulSoup(html, 'html.parser')
            print("searching")


             
            text_elements = soup.find_all(['h1', 'h2', 'p',{'class': 'text-2'}, 'a', 'li', 'span', 'div', {'class': 'wysiwyg text-1'},'b','em','td','strong','section','header','footer','i','ul','button','href','time','figcaption'], text=True)

             

            print("translating")
            for element in text_elements:
                try:
                    text = element.string
                    

                    translated_text = translate(str(text), 'hi')
                    print(f'{text} - {translated_text}')
                    element.string.replace_with(translated_text)
                except:
                    pass

            print("writing")
            
            output_path = os.path.join(output_dir, os.path.basename(root), file)
            os.makedirs(os.path.dirname(output_path), exist_ok=True)
            
     
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(str(soup))
            print("done")