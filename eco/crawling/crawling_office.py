from bs4 import BeautifulSoup
from selenium import webdriver
import random

driver = webdriver.Chrome('/Users/euna/Downloads/chromedriver 2')
driver.implicitly_wait(5)

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta
#자연상점
driver.get('http://onlyeco.co.kr/category/%EC%82%AC%EB%AC%B4%EC%9A%A9%ED%92%88/54/?cate_no=54&sort_method=5#Product_ListMenu')

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')


trs = soup.select('#contents > div.xans-element-.xans-product.xans-product-normalpackage > div.xans-element-.xans-product.xans-product-listnormal.ec-base-product > ul> li')
for tr in trs:
    a_tag = tr.select_one('div > div.description > div.name > a > span:nth-child(2)')
    if a_tag is not None:
        title = a_tag.text.strip()
        img = tr.select_one('div > div.thumbnail > div.prdImg > a > img')['src']
        img2 = 'http:' + img
        price = tr.select_one('div > div.description > ul > li:nth-child(1) > span:nth-child(2)').text
        url = tr.select_one('div > div.thumbnail > div.prdImg > a')['href']
        url2 = 'http://onlyeco.co.kr' + url
        category = 'office'

        print(title, img2, price, url2, category)


        doc = {
            'title' : title,
            'img' : img2,
            'price' : price,
            'url' : url2,
            'like': 0,
            'category': category
        }
        db.maybes.insert_one(doc)
