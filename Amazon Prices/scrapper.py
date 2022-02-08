import requests
from bs4 import BeautifulSoup


url = 'https://www.amazon.de/ILCE-7M3-Digital-Megapixel-Display-Viewfinder/dp/B07B4L1PQ8/' \
      'ref=sr_1_3?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=sony+a7+ilce&qid=1594387292&sr=8-3'

headers = {"User-Agent" : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/83.0.4103.116 Safari/537.36'}

page = requests.get(url, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')
#print(soup.prettify())

title = soup.find('div', attrs={'id': 'titleSection'})
print(title)