import requests
import concurrent.futures
import urllib.request
import pandas as pd

resp = requests.get('https://grocery.walmart.com/v4/api/products/browse?count=60&offset=0&page=1&storeId=2086&taxonomyNodeId=1255027787131_1255027788181')
#print(resp.json())
data = resp.json()
#print(data['products'])
items = [item['USItemId'] for item in data['products']]
#print(items)
    #print(item['USItemId'])
    #item_id = item['USItemId']

# Retrieve a single page and report the URL and contents
def load_url(item):
    #print(item)
    res = requests.get('https://grocery.walmart.com/v3/api/products/' + item + '?itemFields=all&storeId=2086')
    data = res.json()
    dummy_dict = dict()
    dummy_dict['item'] = item
    dummy_dict['sku'] = data.get('sku')
    dummy_dict['offerId'] = data.get('offerId')
    dummy_dict['name'] = data.get('basic', {}).get('name')
    return dummy_dict

result = []
# We can use a with statement to ensure threads are cleaned up promptly
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    # Start the load operations and mark each future with its URL
    future_to_url = {executor.submit(load_url, item): item for item in items}
    for future in concurrent.futures.as_completed(future_to_url):
        url = future_to_url[future]
        try:
            data = future.result()
        except Exception as exc:
            print('%r generated an exception: %s' % (url, exc))
        else:
            if data:
                result.append(data)

if result:
    df = pd.DataFrame(result)
    df.to_excel('Walmart_excel.xlsx', index=False)





