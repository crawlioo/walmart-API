import os
import cloudscraper
import requests
from bs4 import BeautifulSoup

from .utils.helper import rotate_proxy, rotate_user_agent
from projects.config import BaseConfig

url: str = "https://www.walmart.com/search?"
base_url: str = "https://www.walmart.com"

session = requests.session()

headers: dict = {"user-agent": f"{rotate_user_agent()}"}

scraper = cloudscraper.create_scraper(
    sess=session,
    browser={
        'browser': 'chrome',
        'platform': 'windows',
        'mobile': False
    }
)


# ambil itemnya dulu
def get_all_item(keywords: str):
    product_list: list = []
    params: dict = {
        "q": keywords.replace(' ', '+'),
    }

    res = scraper.get(url, params=params, headers=headers)

    print(f"Response Status Code: {res.status_code}")

    # Check status code
    try:
        os.mkdir(f'{os.path.join(BaseConfig.BASE_DIR, "temp")}')
    except FileExistsError:
        pass

    f = open(f'{os.path.join(BaseConfig.BASE_DIR, "temp/res_item.html")}', "w+")
    f.write(res.text)
    f.close()

    # Bypass BOT
    with open(f'{os.path.join(BaseConfig.BASE_DIR, "temp/res_item.html")}', "r") as html_file:
        soup = BeautifulSoup(html_file, 'html.parser')
        bot = soup.find('title')
        while bot.text.strip() == 'Robot or human?':
            # implement proxy
            res = scraper.get(url, params=params, headers=headers, proxies=rotate_proxy())
            soup = BeautifulSoup(res.text, 'html.parser')

        # scraping process
        headers_contents = soup.find('div', attrs={
            'class': 'flex flex-wrap w-100 flex-grow-0 flex-shrink-0 ph2 pr0-xl pl4-xl mt0-xl mt3'})
        contents = headers_contents.find_all('div', attrs={'data-testid': "list-view"})
        for content in contents:
            title = content.find('span', attrs={'class': 'f6 f5-l normal dark-gray mb0 mt1 lh-title'}).text.strip()
            try:
                price = content.find('div', attrs={'class': 'b f5 f4-l black mr1 lh-copy'}).text.strip()
            except:
                price = content.find('div', attrs={'class': 'b black f5 mr1 mr2-xl lh-copy f4-l',
                                                   'aria-hidden': 'true'}).text.strip()

            link = soup.find('a', attrs={'class': 'absolute w-100 h-100 z-1'})['href']
            rating = soup.find('div', attrs={'class': 'mt2 flex items-center'}).find('span', attrs={
                'class': 'w_A5'}).text.strip()

            # sorting data
            data_dict: dict = {
                'title': title,
                'price': price,
                'link': base_url + link,
                'rating': rating,

            }
            product_list.append(data_dict)

        return product_list


def process_scraper(keywords):
    results: list = get_all_item(keywords=keywords)
    return results