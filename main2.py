import os
import requests
from urllib.parse import urlparse
from lxml.html import fromstring

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
        os.chmod('classcentral', 0o777)

    # Guardar el archivo HTML
    with open('classcentral/index.html', 'w', encoding='utf-8') as f:
        f.write(response.text)

    # Parsear el archivo HTML con lxml
    root = fromstring(response.content)
    css_links = []
    js_links = []

    # Encontrar los enlaces a archivos CSS y JavaScript
    for link in root.xpath('//link'):
        
        href = link.attrib.get('href')
        
        if href and href.endswith('.css'):
            print(href)
            css_links.append(href)
    for script in root.xpath('//script'):
        src = script.attrib.get('src')
        if src and src.endswith('.js'):
            js_links.append(src)

    # Guardar los archivos CSS
    for css_link in css_links:
        
        css_url = urlparse(css_link)
        if not css_url.scheme:
            css_url = urlparse(url)
            css_link = css_url.scheme + '://' + css_url.netloc + css_link
        css_response = requests.get(css_link, headers=headers)

        with open(f'classcentral/other.txt', 'wb') as f:
            f.write(css_response.content)
        
    # Guardar los archivos JavaScript
    for js_link in js_links:
        js_url = urlparse(js_link)
        if not js_url.scheme:
            js_url = urlparse(url)
            js_link = js_url.scheme + '://' + js_url.netloc + js_link
        js_response = requests.get(js_link, headers=headers)
        with open(f'classcentral/java.js', 'wb') as f:
            f.write(js_response.content)

    print('Archivos guardados correctamente.')
else:
    # Imprimir un mensaje de error si la solicitud falló
    print('Error al descargar la página web. Código de estado:', response.status_code)
