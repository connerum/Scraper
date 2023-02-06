from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup
import time
import pandas as pd

driver = webdriver.Chrome('chromedriver.exe')

soup = BeautifulSoup(driver.page_source, 'lxml')
boxes = soup.find_all('li', class_='reusable-search__result-container')

df = pd.DataFrame({'Link': [''], 'Name': [''], 'Title': [''], 'Location': ['']})


def main():
    print('Please log into LinkedIn after the browser opens!')
    input('Press enter to open browser.....')
    openBrowser()
    search()


def openBrowser():
    driver.get('https://www.linkedin.com/')
    input('After Logging in, press enter to continue!')


def search():
    driver.get('https://www.linkedin.com/')
    searchQuery = input('Enter the people you would like to search > ')


def scrape():
    counter = 1
    while counter < 100:
        for i in boxes:
            try:
                name = i.find('span', class_ = 'entity-result__title-text t-16').find('span', {'arial-hidden':'true'}).text
            except:
                pass
        counter += 1
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
if __name__ == '__main__':
    main()
