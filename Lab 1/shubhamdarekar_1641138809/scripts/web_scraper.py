import requests
import bs4
from selenium import webdriver
from time import sleep

url = "https://www.cnbc.com/world/?region=world"

def scrape_using_selenium(url):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome(options=options)
    driver.get(url)
    sleep(5)

    soup = bs4.BeautifulSoup(driver.page_source, 'html.parser')
    
    with open("data/raw_data/web_data.html", 'w', encoding='utf-8') as file:
        file.write(soup.prettify())

    driver.quit()

    return soup

print(scrape_using_selenium(url))
