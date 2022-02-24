# Scraping disini

import requests
from bs4 import BeautifulSoup

url = 'https://www.walmart.com/search?q=komputer'
headers = {
    'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'}

def get_all_items():
    # is used to data scraping item like price, and item do you want to scrape
    params = {
    'q' : 'komputer',

    }
    r = requests.get(url, params=params, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')

    pages = []
    results = soup.find('div', {'class':'flex flex-wrap w-100 flex-grow-0 flex-shrink-0 ph2 pr0-xl pl4-xl mt0-xl mt3'})
    contents = results.find_all('div', {'class':'h-100 pb1-xl pr4-xl pv1 ph1'})

    #print(contents)
    for content in contents:
        title = content.find('span', {'class':'w_DX'}).text.strip()
        data_dict = {
            'title': title,
        }
        pages.append(data_dict)
    print(pages)

    # for i in headers_contents:
    #     pages.append(int(i.text))

    # #print(headers_contents)
    # total_pages = max(pages)
    # print('Total pages input:', total_pages)
    # return total_pages







if __name__ == '__main__':
    get_all_items()