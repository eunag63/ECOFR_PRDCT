from bs4 import BeautifulSoup
from selenium import webdriver
import random

#selenium 쓰기 위해서는 Chrome driver 설치
driver = webdriver.Chrome('/Users/euna/Downloads/chromedriver 2')
driver.implicitly_wait(5)

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbproject
# 가치솝
driver.get('https://gachisoap.modoo.at/?link=5d1cpnii')

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')


trs = soup.select('#modoo-q9s2g1 > div > div > div > ul > li')
for tr in trs:
    a_tag = tr.select_one('a > div.title_area')
    if a_tag is not None:
        title = a_tag.text.strip()
        img = tr.select_one('a > div.thumb_area > img')['src']
        img2 = 'http:' + img
        price = tr.select_one('span:nth-child(2)').text
        url = tr.select_one('a')['href']
        url2 = 'http://onlyeco.co.kr' + url
        category = random.randint(1, 5)

        print(title, img2, price, url2, category)


        doc = {
            'title' : title,
            'img' : img2,
            'price' : price,
            'url' : url2,
            'like': 0,
            'category': category
        }
        db.crawling.insert_one(doc)