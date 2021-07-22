from bs4 import BeautifulSoup
from selenium import webdriver
import random

#selenium 쓰기 위해서는 Chrome driver 설치
driver = webdriver.Chrome('/Users/euna/Downloads/chromedriver 2')
driver.implicitly_wait(5)

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta
# 덕분애 제로웨이스트샵
driver.get('https://www.thanksto.co.kr/goods/goods_list.php?cateCd=009005&sort=date&pageNum=20')


html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')


trs = soup.select('#contents > div > div > div.goods_list_item > div.goods_list > div > div > ul > li')

for tr in trs:
    a_tag = tr.select_one('div > div.item_info_cont > div.item_tit_box > a > strong')
    if a_tag is not None:
        title = a_tag.text.strip()
        img = tr.select_one('div > div.item_photo_box > a > img')['src']
        img2 = 'https://www.thanksto.co.kr' + img
        price = tr.select_one('div > div.item_info_cont > div.item_money_box > strong > span').text
        url = tr.select_one('div > div.item_photo_box > a')['href']
        url2 = 'https://www.thanksto.co.kr' + url[2:]
        category = 'bathroom'

        print(title,img2,price,url2,category)

        doc = {
            'title' : title,
            'img' : img2,
            'price' : price,
            'url' : url2,
            'like': 0,
            'category': category
        }
        db.maybes.insert_one(doc)