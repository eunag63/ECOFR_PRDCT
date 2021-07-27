from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome('/Users/euna/Downloads/chromedriver 2')
driver.implicitly_wait(5)

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbproject
#커뮤니티1
driver.get('https://magazine.cheil.com/?s=%EC%A0%9C%EB%A1%9C%EC%9B%A8%EC%9D%B4%EC%8A%A4%ED%8A%B8&after_year=2020&after_month=1&before_year=&before_month=')

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')


#content > section > div > div:nth-child(2) > a > img
#content > section > div > div:nth-child(2) > div > div > h6 > a
#content > section > div > div:nth-child(2) > a
trs = soup.select('#content > section > div > div')
for tr in trs:
    a_tag = tr.select_one('div > div > h6 > a')
    if a_tag is not None:
        title = a_tag.text.strip()
        img = tr.select_one('a > img')['src']
        url = tr.select_one('a')['href']

        print(title,img,url)
        doc = {
            'title' : title,
            'img' : img,
            'url' : url,
        }
        db.columns.insert_one(doc)