from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbproject



## HTML을 주는 부분
@app.route('/')
def home():
   return render_template('index.html')

## 전체 보여주기
@app.route('/re', methods=['GET'])
def listing():
    product = list(db.crawling.find({},{'_id':False}))
    return jsonify({'products':product})

## 카테고리 living만 보여주기
@app.route('/living')
def getLiving():
   return render_template('index_living.html')
@app.route('/living/re', methods=['GET'])
def cate_living():
    product = list(db.crawling.find({'category':'living'}, {'_id': False}))
    return jsonify({'products':product})

## 카테고리 kitchen만 보여주기
@app.route('/kitchen')
def getKitchen():
   return render_template('index_kitchen.html')
@app.route('/kitchen/re', methods=['GET'])
def cate_kitchen():
    product = list(db.crawling.find({'category':'kitchen'}, {'_id': False}))
    return jsonify({'products':product})

## 카테고리 office만 보여주기
@app.route('/office')
def getOffice():
   return render_template('index_office.html')
@app.route('/office/re', methods=['GET'])
def cate_office():
    product = list(db.crawling.find({'category':'office'}, {'_id': False}))
    return jsonify({'products':product})

## like 순으로 배열하는 기능
@app.route('/eco', methods=['GET'])
def showArticles():
    like_heart = list(db.crawling.find({}, {'_id': False}).sort('like', -1))
    return jsonify({'likes_heart': like_heart})
## like 해당하는 제목찾아서 그 제목의 like 쌓는 기능
@app.route('/eco', methods=['POST'])
def like_heart():
    title_receive = request.form['title_give']
    target_prodct = db.crawling.find_one({'title': title_receive})
    current_like = target_prodct['like']
    new_like = current_like + 1
    db.crawling.update_one({'title': title_receive}, {'$set': {'like': new_like}})
    return jsonify({'msg': '좋아요 완료!'})


if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)

