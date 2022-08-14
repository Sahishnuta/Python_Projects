import numpy as np
import pandas as pd
from scrapy.selector import Selector
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from tqdm import tqdm
import warnings
warnings.filterwarnings("ignore")

driver = webdriver.Chrome('chromedriver.exe')
url = 'https://www.imdb.com/title/tt0241527/reviews?ref_=tt_sa_3'
time.sleep(1)
driver.get(url)
time.sleep(1)
print(driver.title)
time.sleep(1)
body = driver.find_element(By.CSS_SELECTOR, 'body')
body.send_keys(Keys.PAGE_DOWN)
time.sleep(1)
body.send_keys(Keys.PAGE_DOWN)
time.sleep(1)
body.send_keys(Keys.PAGE_DOWN)

sel = Selector(text=driver.page_source)
review_counts = sel.css('.lister .header span::text').extract_first().replace(',', '').split(' ')[0]
more_review_pages = int(int(review_counts)/25)

for i in tqdm(range(more_review_pages)):
    try:
        css_selector = 'load-more-trigger'
        driver.find_element(By.ID, css_selector).click()
    except:
        pass

reviews = driver.find_elements(By.CSS_SELECTOR, 'div.review-container')
first_review = reviews[0]
sel2 = Selector(text=first_review.get_attribute('innerHTML'))
rating = sel2.css('.rating-other-user-rating span::text').extract_first().strip()
review = sel2.css('.text.show-more__control::text').extract_first().strip()
review_date = sel2.css('.review-date::text').extract_first().strip()
author = sel2.css('.display-name-link a::text').extract_first().strip()
review_title = sel2.css('a.title::text').extract_first().strip()
review_url = sel2.css('a.title::attr(href)').extract_first().strip()
helpfulness = sel2.css('.actions.text-muted::text').extract_first().strip()
print('nRating:',rating)
print('nreview_title:',review_title)
print('nAuthor:',author)
print('nreview_date:',review_date)
print('nreview:',review)
print('nhelpfulness:',helpfulness)
