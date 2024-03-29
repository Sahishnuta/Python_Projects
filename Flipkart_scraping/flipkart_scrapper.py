import bs4
from bs4 import BeautifulSoup as bs
from numpy import append
import requests
import pandas as pd


link='https://www.flipkart.com/search?q=tv&as=on&as-show=on&otracker=AS_Query_TrendingAutoSuggest_8_0_na_na_na&otracker1=AS_Query_TrendingAutoSuggest_8_0_na_na_na&as-pos=8&as-type=TRENDING&suggestionId=tv&requestId=9c9fa553-b7e5-454b-a65b-bbb7a9c74a29'

page = requests.get(link)
#print(page.content)
soup = bs(page.content, 'html.parser')
#print(soup.prettify())

products=[]              #List to store the name of the product
prices=[]                #List to store price of the product
ratings=[]               #List to store rating of the product
apps = []                #List to store supported apps                
os = []                  #List to store operating system
hd = []                  #List to store resolution
sound = []               #List to store sound output

for data in soup.findAll('div', class_='_3pLy-c row') :
    name=data.find('div', attrs = {'class' : "_4rR01T"})
    #get price of the product
    price=data.find('div', attrs = {'class' : '_30jeq3 _1_WHN1'})
    #get rating of a product
    rating=data.find('div', attrs = {'class' : "_3LWZlK"})
    #get other details and specifications of the product
    specification=data.find('div', attrs = {'class' : "fMghEO"})
    for each in specification:
        col=each.find_all('li', attrs = {'class' : 'rgWa7D'})
        app = col[0].text
        os_ = col[1].text
        hd_ = col[2].text
        sound_ = col[3].text

    products.append(name.text)
    prices.append(price.text)
    apps.append(app)
    os.append(os_)
    hd.append(hd_)
    sound.append(sound_)
    ratings.append(rating.text)

#printing the length of list
print(len(products))
print(len(ratings))
print(len(prices))
print(len(apps))
print(len(sound))
print(len(os))
print(len(hd))


df=pd.DataFrame({'Product Name':products,'Supported_apps':apps,'sound_system':sound,'OS':os,"Resolution":hd,'Price':prices,'Rating':ratings})
df.head(10)
print(df.head())
df.to_csv('flipkart_data.csv', index=False)