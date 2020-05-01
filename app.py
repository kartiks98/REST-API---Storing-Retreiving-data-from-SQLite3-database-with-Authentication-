# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 00:52:40 2020

@author: Kartik Saini
"""


from flask import Flask,request
from flask_restful import Resource, Api,reqparse
from flask_jwt import JWT,jwt_required
from security import authenticate,identity

app=Flask(__name__)
api=Api(app)
app.secret_key='key'
jwt=JWT(app,authenticate,identity)

items=[]

class Item(Resource):
    parser=reqparse.RequestParser()
    parser.add_argument('price', 
                            type=float,
                            required=True,
                            help=f'{"price"} is a required field')
    
    def post(self, name):
        # data=request.get_json()
        # parser=reqparse.RequestParser()
        # parser.add_argument('price', 
        #                     type=float,
        #                     required=True,
        #                     help=f'{"price"} is a required field')
        
        for item in items:
            if item['name']==name:                          #filter method can
                return {'item':'already exist'}, 400        #also  be used instead
        
        data=Item.parser.parse_args()
        
        item={'name':name,'price':data['price']}
        items.append(item)
        return item,201
    
    @jwt_required()
    def get(self, name):
        for item in items:
            if item['name']==name:
                return item
        return {'item':None},404
    
    def put(self, name):
        # data=request.get_json()
        # parser=reqparse.RequestParser()
        # parser.add_argument('price', 
        #                     type=float,
        #                     required=True,
        #                     help=f'{"price"} is a required field')
        
        data=Item.parser.parse_args()
        
        for item in items:
            if item['name']==name:
                item.update(data)
                return item
        item={'name':name,'price':data['price']}
        items.append(item)
        return item,201
    
    def delete(self, name):
        global items
        new_items=[]
        yes=False
        for item in items:
            if item['name']==name:
                yes=True
        if yes==True:
            for item in items:
                if item['name']!=name:
                    new_items.append(item)
            items=new_items
            return {name:'deleted'}
        else:
            return {'item':None},404
    
class Items(Resource):
    def get(self):
        return {'items':items}



api.add_resource(Item, '/item/<string:name>')
api.add_resource(Items, '/items')

app.run(port=5000)