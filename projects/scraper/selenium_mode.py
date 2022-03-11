import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

website = "https://www.walmart.com/search?q=computer"

def get_total_pages(keywords):
    # used to search total pages

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    actions = ActionChains(driver)
    next_page_btn = driver.find_element(By.XPATH, ('//li[@aria-label="false"]//a'))
    actions.move_to_element(next_page_btn).perform()
    time.sleep(0.5)
    next_page_btn.click()
    # get url
    driver.get(website)

    pages_source = driver.page_source
    soup = BeautifulSoup(pages_source, 'html.parser')

    pages =[]

def get_all_items():

    options = Options()
    options.add_argument("start-maximized")

    #avoiding detection
    options.add_argument('--disable-blink-features=AutomationControlled')
    driver = webdriver.Chrome( options=options, service=Service (ChromeDriverManager().install()))

    # get url
    driver.get(website)

    pages_source = driver.page_source
    soup = BeautifulSoup(pages_source, 'html.parser')
    product_list: list = []
    #scraping proccess
    headers_contents = soup.find('div', attrs={'class':'flex flex-wrap w-100 flex-grow-0 flex-shrink-0 ph2 pr0-xl pl4-xl mt0-xl mt3'})
    contents = headers_contents.find_all('div', attrs={'data-testid':'list-view'})
    for content in contents:

        title = content.find('span', attrs={'class':'f6 f5-l normal dark-gray mb0 mt1 lh-title'}).text.strip()
        try:
            price = content.find('div', attrs={'class': 'b f5 f4-l black mr1 lh-copy'}).text.strip()
        except:
            price = content.find('div', attrs={'class' :'b black f5 mr1 mr2-xl lh-copy f4-l', 'aria-hidden': 'true'}).text.strip()
        link = soup.find('a', attrs={'class': 'absolute w-100 h-100 z-1'})['href']
        try:
            rating = soup.find('div', attrs={'class': 'mt2 flex items-center'}).find('span', attrs={'class': 'w_A5'}).text.strip()
        except:
            rating = soup.find('span', attrs={'w_R'}).text.strip()

        data_dict : dict ={
            'title' : title,
            'price': price,
            'link': link,
            'rating': rating,

        }
        print(data_dict)

        product_list.append(data_dict)




if __name__ == '__main__':
    get_total_pages()
    get_all_items()
