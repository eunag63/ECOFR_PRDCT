from bs4 import BeautifulSoup
from selenium import webdriver
import random

driver = webdriver.Chrome('/Users/euna/Downloads/chromedriver 2')
driver.implicitly_wait(5)

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta
#더피커
driver.get('https://thepicker.net/LIVING')

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

trs = soup.select('#container_w20200520f9978e7d73dac > div')
for tr in trs:
    a_tag = tr.select_one('div.item-detail > div.item-pay > h2 > a')
    if a_tag is not None:
        title = a_tag.text.strip()
        img = tr.select_one('div.item-wrap > a > img._org_img.org_img._lazy_img')['data-original']
        price = tr.select_one('div.item-detail > div.item-pay > div.item-pay-detail > p.pay.inline-blocked').text.strip()
        url = tr.select_one('div.item-wrap > a')['href']
        url2 = 'https://thepicker.net' + url
        category = 'living'

        print(title, img, price, url2, category)

        doc = {
            'title' : title,
            'img' : img,
            'price' : price,
            'url' : url2,
            'like' : 0,
            'category': category

        }
        db.maybes.insert_one(doc)

