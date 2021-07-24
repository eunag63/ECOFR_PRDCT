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

if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)

