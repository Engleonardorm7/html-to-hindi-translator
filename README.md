# Program to translate HTML files

This program takes as input a base directory containing HTML files and uses the BeautifulSoup library to extract the text elements from the files. It then uses the mtranslate library to translate these text elements into Hindi.

The program looks for text elements in HTML tags such as h1, h2, p, a, li, span, div, b, em, td, strong, section, header, footer, i, ul, button, href, time, and figcaption .

After the text elements are translated, the program replaces the original elements in the HTML files and saves them to a specified output directory.
