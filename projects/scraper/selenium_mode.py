import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

base_url: str = "https://www.walmart.com"


def get_total_pages(keypass):
    # used to search total pages

    website = f'https://www.walmart.com/search?q={keypass}'
    options = Options()
    # options.headless = True

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # get url
    driver.get(website)
    # maximize_windows
    driver.maximize_window()

    # pagination
    pages_source = driver.page_source

    # temporary file
    f = open("selenium_mode.html", "w+")
    f.write(pages_source)
    f.close()

    # scraping process
    soup = BeautifulSoup(pages_source, 'html.parser')
    pages = []
    data = []
    # handle pagination
    headers_contents = soup.find('ul', attrs={'class': 'list flex items-center justify-center pa0'}).find_all('li')
    for i in headers_contents:
        data.append(i.text)

    for i in data:
        if i.isnumeric():
            pages.append(int(i))
    total_pages = max(pages)
    print('Total pages yang didapatkan:', total_pages)
    return total_pages


def get_all_items(keypass, pages):
    website = f'https://www.walmart.com/search?q={keypass}&page={pages}&affinityOverride=default'
    options = Options()
    options.add_argument("start-maximized")

    # avoiding detection
    options.add_argument('--disable-blink-features=AutomationControlled')
    # options.headless = True

    driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))

    # get url
    driver.get(website)

    pages_source = driver.page_source
    soup = BeautifulSoup(pages_source, 'html.parser')
    product_list: list = []
    # scraping proccess
    headers_contents = soup.find('div', attrs={
        'class': 'flex flex-wrap w-100 flex-grow-0 flex-shrink-0 ph2 pr0-xl pl4-xl mt0-xl mt3'})
    try:

        contents = headers_contents.find_all('div', attrs={'data-testid': 'list-view'})
    except:
        contents = headers_contents.find_all('div', attrs={'h2 relative mb2'})
    for content in contents:

        title = content.find('span', attrs={'class': 'f6 f5-l normal dark-gray mb0 mt1 lh-title'}).text.strip()
        try:
            price = content.find('div', attrs={'class': 'b f5 f4-l black mr1 lh-copy'}).text.strip()
        except:
            try:
                price = content.find('div', attrs={'aria-hidden': 'true'}).text.strip()
            except:
                try:
                    price = content.find('ul', attrs={'list flex items-center justify-center pa0'}).text.strip()
                except:
                    price = content.find('li', attrs={'aria-hidden="false"'})
        link = soup.find('a', attrs={'class': 'absolute w-100 h-100 z-1'})['href']
        try:
            rating = soup.find('div', attrs={'class': 'mt2 flex items-center'}).find('span', attrs={
                'class': 'w_A5'}).text.strip()
        except:
            rating = soup.find('span', attrs={'w_R'}).text.strip()

        data_dict: dict = {
            'title': title,
            'price': price,
            'link': base_url +link,
            'rating': rating,

        }
        print(data_dict)
        product_list.append(data_dict)

    return product_list


def get_detail_pages(url):
    options = Options()

    driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))

    driver.get(url)

    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'html.parser')
    # temporary file
    f = open("detail_page.html", "w+")
    f.write(page_source)
    f.close()

    produc_detail: list = []
    # scraping proccess

    title = soup.find('h1', attrs={'class': 'f3 b lh-copy dark-gray mt1 mb2'}).text.strip()
    price = soup.find('span', attrs={'class': 'b lh-copy dark-gray mr2 f1'}).text.strip()
    rating = soup.find('div', attrs={'class': 'flex flex-row items-center justify-end h2'}).find('span', attrs={
        'class': 'w_R'}).text.strip()

    detail_pages = {
        'title': title,
        'price': price,
        'rating': rating,
    }
    print(detail_pages)
    return produc_detail


def main(keypass):
    final_result = []

    total_pages = get_total_pages(keypass)
    for page in range(total_pages):
        page += 1
        print(f'Scraping halaman ke:{page}')
        products = get_all_items(keypass, page)
        final_result += products
    # proccess data here
    total_data = len(final_result)

    print('Ini adalah total halaman yang sudah di scrape '.format(total_data))
    for result in final_result:
        get_detail_pages(result['link'])


if __name__ == '__main__':
    keypass = 'computer'  # <bisa diganti input
    main(keypass)
