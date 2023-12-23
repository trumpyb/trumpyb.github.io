import os
from requests.exceptions import ConnectionError
import requests
import replit
from bs4 import BeautifulSoup

replit.clear()

website = input('Input Website\n')

try:
    page = requests.get(website)
except ConnectionError:
    print('Error')
    exit()

html = BeautifulSoup(page.content, "html.parser")

replit.clear()
open('index.html','w').write(str(html))

os.system('clear')

print('https://trumpyb.github.io/prog/website/site.html')
