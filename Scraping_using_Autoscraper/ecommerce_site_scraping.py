# Importing AutoScraper
from autoscraper import AutoScraper


URL = 'https://www.bookswagon.com/'
# create a list of elements
items = ['Rs.518' , 'My First Library: Boxset of 10 Board Books for Kids']

# create object
scrape = AutoScraper()
# feeding for scraping
final_result = scrape.build(URL,items)
# display result
print(final_result)


item = ['https://d2g9wbak88g7ch.cloudfront.net/productimages/mainimages/266/9789387779266.jpg','My First Library: Boxset of 10 Board Books for Kids']
# creating object
scrap = AutoScraper()
# building result
final_result = scrap.build( URL, item )
# display result
print(final_result)

