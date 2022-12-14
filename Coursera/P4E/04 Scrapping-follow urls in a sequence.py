# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
count = input('Enter count: ')
pos = input('Enter position: ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
# Se cambia el tag según sea necesario

# El ejercicio consistia en entrar al url, sacar sus datos que eran más urls y luego seguir dichos urls dependiendo de la posición y un número dado de veces
x = 0
tags = soup('a')
print('Retrieving:', url)
while x < int(count):
    y = 0
    for tag in tags:
        y = y + 1
        if y == int(pos):
            url = tag.get('href', None)
            break
            
    print('Retrieving:', url)
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")
    tags = soup('a')
    x = x + 1
    y = 0

print('\nName:', tag.contents[0])

#NOTA TURBO CRACK: PORQUE SOY MARICA, SE ME OLVIDÓ QUE EXISTE EL 'for x in range()' PARA HACER EL FOR EN UN RANGO DETERMINADO