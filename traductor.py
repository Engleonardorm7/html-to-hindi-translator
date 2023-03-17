from bs4 import BeautifulSoup
from googletrans import Translator

print("starting")
# Leer el archivo HTML
with open ('./pagina traducida/www.classcentral.com/index.html', 'r', encoding='utf-8') as f:
    print("reading")
    html = f.read()
    

# Crear un objeto BeautifulSoup para analizar el HTML
soup = BeautifulSoup(html, 'html.parser')
print("searching")
span_tags = soup.find_all('a', class_='head-3 weight-semi line-tight color-charcoal')

for span_tag in span_tags:
    
    try:
        text = span_tag.string
        print(text)

        translator = Translator()
        translated_text = translator.translate(str(text), dest='hi').text
        text.replace_with(translated_text)
    except:
        pass
print("writing")
# Escribir el contenido modificado en un nuevo archivo HTML
with open('translated_page.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))
print("done")


# text_tags = soup.find_all(string=True)

# # Traducir el texto de cada etiqueta al hindi
# translator = Translator()
# print("Translating")
# for tag in text_tags:
#     try:
#         translated_text = translator.translate(str(tag), dest='hi').text
#         tag.replace_with(translated_text)
#     except:
#         pass
# print("writing")
# # Escribir el contenido modificado en un nuevo archivo HTML
# with open('translated_page.html', 'w', encoding='utf-8') as f:
#     f.write(str(soup))
# print("done")


#_________________________________________________________
#text = soup.find("span","class=padding-right-xxsmall").all().get_text.()  # por ejemplo, todas las etiquetas <h2>

# Recorrer las etiquetas y reemplazar el texto

    #etiqueta.string = "Nuevo texto"  # reemplazar "Nuevo texto" por el texto deseado
#print(text)
# Imprimir el HTML modificado
#print(soup.prettify())