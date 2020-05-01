# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 00:52:40 2020

@author: Kartik Saini
"""


from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate,identity
from user import UserReg
from item import Item,Items
from db import db

app=Flask(__name__)
app.config['SQLAlCHEMY_DATABASE_URI']='sqlite:///MyData.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
api=Api(app)
app.secret_key='key'
jwt=JWT(app,authenticate,identity)

@app.before_first_request
def create_table():
    db.create_all()

api.add_resource(Item, '/item/<string:name>')
api.add_resource(Items, '/items')
api.add_resource(UserReg,'/register')

db.init_app(app)
app.run(port=5000)