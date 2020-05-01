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

app=Flask(__name__)
api=Api(app)
app.secret_key='key'
jwt=JWT(app,authenticate,identity)


api.add_resource(Item, '/item/<string:name>')
api.add_resource(Items, '/items')
api.add_resource(UserReg, '/register')

app.run(port=5000)