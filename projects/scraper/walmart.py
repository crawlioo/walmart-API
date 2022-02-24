import os
import requests
from bs4 import BeautifulSoup
from utils.helper import rotate_user_agent

url: str = "https://www.walmart.com/search?"

headers: dict = {'user-agent': rotate_user_agent()}

# ambil itemnya dulu
def get_all_item(keywords: str):
    params: dict = {
        'q': keywords,
    }
    res = requests.get(url, params=params, headers=headers)

    # Check status code
    try:
        os.mkdir('temp')
    except FileExistsError:
        pass
    
    f = open('temp/item_res.html', 'w+')
    f.write(res.text)
    f.close()

    soup = BeautifulSoup(res.text, 'html.parser')

    # scraping process
    headers_content = soup.find('div', attrs={"class": "flex flex-wrap w-100 flex-grow-0 flex-shrink-0 ph2 pr0-xl pl4-xl mt0-xl mt3"})
    contents = headers_content.find_all('div', attrs={'class':'mb1 ph1 pa0-xl bb b--near-white w-25'})
    for content in contents:
        try:
            title = content.find('span', attrs={'class': "w_DX"}).text.strip()
        except:
            raise Exception(title)
        try:
            link = content.find('a', attrs={'class': 'absolute w-100 h-100 z-1'})['href']
        except:
            raise Exception(link)
        try:
            price = content.find('div', attrs={'class':'b black f5 mr1 mr2-xl lh-copy f4-l', 'aria-hidden': 'true'}).text
        except:
            raise Exception(price)
        try:
            rating = content.find('div', attrs={'class':'mt2 flex items-center'}).find('span', attrs={'class':'mt2 flex items-center'}).text
        except:
            raise Exception(rating)

        data_dict: dict = {
            'title': title,
            'product url': link,
            'price': price,
            'rating': rating
        }