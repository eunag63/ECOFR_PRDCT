from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome('/Users/euna/Downloads/chromedriver 2')
driver.implicitly_wait(5)

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbproject
#커뮤니티1
driver.get('http://m.kyeongin.com/kiib/searchMobile.php?tsearch=%EC%A0%9C%EB%A1%9C%20%EC%9B%A8%EC%9D%B4%EC%8A%A4%ED%8A%B8')

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

trs = soup.select('#articleArea')
for tr in trs:
    a_tag = tr.select_one('dl:nth-child(1)')
    if a_tag is not None:
        title = a_tag.text.strip()
        img = tr.select_one('dl:nth-child(1) > dd.img')['data-original']
        url = tr.select_one('dl:nth-child(1) > dd.img > a')['href']
        url2 = 'https://m.kyeongin.com/' + url

        doc = {
            'title' : title,
            'img' : img,
            'url' : url2,
        }
        db.columns.insert_one(doc)