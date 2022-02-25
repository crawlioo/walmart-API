# Scraping disini
import os
import requests
from bs4 import BeautifulSoup

url: str = 'https://www.walmart.com/search?'

headers: dict = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'}


def get_all_items(keywords: str):
    # is used to data scraping item like price, and item do you want to scrape
    params: dict = {
        'q': keywords,

    }
    r = requests.get(url, params=params, headers=headers)
    # check status_code
    try:
        os.mkdir('temp')
    except FileExistsError:
        pass
    f = open('temp/item_res.html', 'w+')
    f.write(r.text)
    f.close()

    soup = BeautifulSoup(r.text, 'html.parser')

    # scraping proccess
    pages = []
    results = soup.find('div', {'class': 'flex flex-wrap w-100 flex-grow-0 flex-shrink-0 ph2 pr0-xl pl4-xl mt0-xl mt3'})
    contents = results.find_all('div', {'class': 'mb1 ph1 pa0-xl bb b--near-white w-25'})

    # print(contents)
    for content in contents:
        title = content.find('span', attrs={'class': 'f6 f5-l normal dark-gray mb0 mt1 lh-title'}).text
        price = content.find('div', attrs={'class': 'b black f5 mr1 mr2-xl lh-copy f4-l', 'aria-hidden': 'true'}).text
        link = content.find('a', attrs={'class': 'absolute w-100 h-100 z-1'})['href']
        review = content.find('div', {'class': 'mt2 flex items-center'}).text
        data_dict = {
            'title': title,
            'price': price,
            'product_url': link,
            'review': review,

        }
        pages.append(data_dict)
    print(pages)

    for i in pages:
        print(i)


if __name__ == '__main__':
    keywords = 'computer'
    get_all_items(keywords)
