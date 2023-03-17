import requests
from bs4 import BeautifulSoup
from googletrans import Translator

# Descargar el contenido de la página web
url = 'https://www.classcentral.com/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

# Realizar una solicitud HTTP GET a la URL con el nuevo agente de usuario
print("starting")
response = requests.get(url, headers=headers)

html_content = response.text

# Parsear el contenido HTML con BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Obtener todas las etiquetas de HTML que contienen texto visible
text_tags = soup.find_all(string=True)

# Traducir el texto de cada etiqueta al hindi
translator = Translator()
for tag in text_tags:
    try:
        translated_text = translator.translate(str(tag), dest='hi').text
        tag.replace_with(translated_text)
    except:
        pass

# Escribir el contenido modificado en un nuevo archivo HTML
with open('translated_page.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))
print("done")