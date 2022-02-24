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
        try:
            price = content.find('div', {'class':'b black f5 mr1 mr2-xl lh-copy f4-l'}).text.strip()
        except:
            price = 'no price'
        try:
            classification = content.find('span', {'class':'f6 f5-l normal dark-gray mb0 mt1 lh-title'}).text.strip()
        except:
            classification = 'no classification'
        try:
            review = content.find('div', {'class': 'flex flex-wrap justify-start items-center lh-title mb2 mb1-m'}).find('span').text
        except:
            review = 'no review'


        data_dict = {
            'title': title,
            'price': price,
            'classification': classification,
            'review': review,


        }
        pages.append(data_dict)
    print(pages)

    for i in pages:
        print(i)

    # #print(headers_contents)
    # total_pages = max(pages)
    # print('Total pages input:', total_pages)
    # return total_pages







if __name__ == '__main__':
    get_all_items()