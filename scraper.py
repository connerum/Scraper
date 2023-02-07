from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
import pandas as pd


driver = webdriver.Chrome('chromedriver.exe')


def main():
    print('Please log into LinkedIn after the browser opens!')
    input('Press enter to open browser.....')
    openBrowser()
    search()
    preScrape()
    scrape()


def openBrowser():
    driver.get('https://www.linkedin.com/')
    input('After Logging in, press enter to continue!')


def search():
    driver.get('https://www.linkedin.com/')
    searchQuery = input('Enter the people you would like to search > ')
    try:
        searchBar = driver.find_element(By.XPATH, '/html/body/div[6]/header/div/div/div/div[1]/input')
        searchBar.click()
        searchBar.send_keys(searchQuery)
        searchBar.send_keys(Keys.RETURN)
        time.sleep(3)
        driver.find_element(By.XPATH, '/html/body/div[6]/div[3]/div[2]/section/div/nav/div/ul/li[1]/button').click()
    except:
        print('Restart Program')


def preScrape():
    print('Before scraping begins, please go to the second page!')
    input('Press enter to continue...')

def scrape():
    df = pd.DataFrame({'Name': [''], 'Link': [''], 'Title': [''], 'Location': ['']})
    counter = 1
    soup = BeautifulSoup(driver.page_source, 'lxml')
    boxes = soup.find_all('li', class_='reusable-search__result-container')
    while counter < 99:
        soup = BeautifulSoup(driver.page_source, 'lxml')
        boxes = soup.find_all('li', class_='reusable-search__result-container')
        for i in boxes:
            try:
                nameDiv = i.find('span', class_='entity-result__title-text t-16').find('span').text
                name = str(nameDiv).split('View')[0]
                link = i.find('a', class_='app-aware-link').get('href')
                title = i.find('div', class_='entity-result__primary-subtitle t-14 t-black t-normal').text.strip()
                location = i.find('div', class_='entity-result__secondary-subtitle t-14 t-normal').text
                df = df.append({'Name': name, 'Link': link, 'Title': title, 'Location': location}, ignore_index=True)
            except:
                pass
        counter += 1
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
        time.sleep(1)
        try:
            driver.find_element(By.XPATH,
                                '/html/body/div[6]/div[3]/div[2]/div/div[1]/main/div/div/div[2]/div/div[2]/div/button[2]').click()
            time.sleep(2)
        except:
            print('error')
    df.to_csv('scrapedInfo.csv')


if __name__ == '__main__':
    main()


