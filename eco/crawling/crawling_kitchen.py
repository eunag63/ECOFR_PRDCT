
from bs4 import BeautifulSoup
from selenium import webdriver
import random

#selenium 쓰기 위해서는 Chrome driver 설치
driver = webdriver.Chrome('/Users/euna/Downloads/chromedriver 2')
driver.implicitly_wait(5)

from pymongo import MongoClient
client = MongoClient('mongodb://test:test@localhost', 27017)
# client = MongoClient('localhost', 27017)
db = client.dbproject

# 지구샵
driver.get('https://www.jigushop.co.kr/kitchen')

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')


#container_w2020010454502ce512f6d > div:nth-child(1) > div.item-wrap > a > img._org_img.org_img._lazy_img
#container_w2020010454502ce512f6d > div:nth-child(2) > div.item-wrap > a > img._org_img.org_img._lazy_img
#container_w2020010454502ce512f6d > div:nth-child(1) > div.item-detail > div.item-pay > h2 > a
#container_w2020010454502ce512f6d > div:nth-child(1) > div.item-detail > div.item-pay > div.item-pay-detail > p.pay.inline-blocked
#container_w2020010454502ce512f6d > div:nth-child(1) > div.item-wrap > a

trs = soup.select('#container_w2020010454502ce512f6d > div')
for tr in trs:
    a_tag = tr.select_one('div.item-detail > div.item-pay > h2 > a')
    if a_tag is not None:
        title = a_tag.text.strip()
        img = tr.select_one('div.item-wrap > a > img._org_img.org_img._lazy_img')['data-original']
        price = tr.select_one('div.item-detail > div.item-pay > div.item-pay-detail > p.pay.inline-blocked').text.strip()
        url = tr.select_one('div.item-wrap > a')['href']
        url2 = 'https://www.jigushop.co.kr' + url
        category = 'kitchen'

        print(title,img,price,url2,category)


        doc = {
            'title' : title,
            'img' : img,
            'price' : price,
            'url' : url2,
            'like': 0,
            'category': category
        }
        db.crawling.insert_one(doc)