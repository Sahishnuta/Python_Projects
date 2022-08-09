from autoscraper import AutoScraper

url = 'https://www.analyticsvidhya.com/blog/category/machine-learning/'
#wanted_list = ['Applications of EdgeML']
wanted_list = ['https://www.analyticsvidhya.com/blog/2022/08/applications-of-edgeml/']
scraper = AutoScraper()
result = scraper.build(url, wanted_list)
print(result)

scraper.save('ml_blogs')

# proxies = {
#     "http": 'http://127.0.0.1:8001',
#     "https": 'https://127.0.0.1:8001',
# }

# result = scraper.build(url, wanted_list, request_args=dict(proxies=proxies))