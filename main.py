import os
import requests
from lxml.html import iterlinks

# URL de la página web original
url = 'https://www.classcentral.com/'

# Configurar un agente de usuario diferente para la solicitud
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

# Realizar una solicitud HTTP GET a la URL con el nuevo agente de usuario
response = requests.get(url, headers=headers)

# Comprobar si la solicitud fue exitosa (código de estado 200)
if response.status_code == 200:
    # Crear un directorio para guardar los archivos descargados
    if not os.path.exists('classcentral'):
        os.makedirs('classcentral')

    # Guardar el archivo HTML
    with open('classcentral/index.html', 'w', encoding='utf-8') as f:
        f.write(response.text)

    # Guardar los archivos CSS
    css_links = []
    for link in iterlinks(response.text):
        if link[2].endswith('.css'):
            css_links.append(link[2])

    for css_link in css_links:
        css_response = requests.get(css_link, headers=headers)
        with open(f'classcentral/{css_link.split("/")[-1]}', 'wb') as f:
            f.write(css_response.content)

    # Guardar los archivos JavaScript
    js_links = []

    # Descargar y guardar archivos JavaScript
    for js_link in js_links:
        if js_link.startswith("//"):
            js_link = "https:" + js_link  # Agregar el esquema 'https:' a la URL
        js_response = requests.get(js_link, headers=headers)
        js_filename = "js/" + js_link.split("/")[-1]
        with open(js_filename, "w", encoding="utf-8") as js_file:
            js_file.write(js_response.text)


    print('Archivos guardados correctamente.')
else:
    # Imprimir un mensaje de error si la solicitud falló
    print('Error al descargar la página web. Código de estado:', response.status_code)
