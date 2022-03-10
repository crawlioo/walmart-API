from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

website = "https://www.walmart.com/search?q=computer"

# searches
driver.get(website)

search_box =  driver.find_element(by=By.NAME, value='q')
search_box.send_keys('Belajar automation testing' + Keys.ENTER)

items = driver.find_element(By.CLASS_NAME, 'w_R')


    # data_dict= {
    #     'title': title,
    #     'price': price,
    #     'link': base_url + link,
    #     'rating': rating,
    #
    # }







