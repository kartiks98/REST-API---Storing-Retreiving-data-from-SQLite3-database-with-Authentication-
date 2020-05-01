# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 17:49:51 2020

@author: Kartik Saini
"""

from flask_restful import Resource,reqparse
from flask_jwt import jwt_required
from db import db

class Item(Resource,db.Model):
    __tablename__='items'
    
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(80))
    price=db.Column(db.Float(80,precision=2))
    
    def __init__(self,name,price):
        self.name=name
        self.price=price
    
    parser=reqparse.RequestParser()
    parser.add_argument('price', 
                            type=float,
                            required=True,
                            help=f'{"price"} is a required field')
    
    def post(self, name):
        data=Item.parser.parse_args()
        check=db.query.filter_by(name=name)
        if check:
            return {f'{name}':'already exists'},400
        item=Item(name,data['price'])
        db.session.add(item)
        db.session.commit()
        return {'name':name,'price':data['price']},201
        
    
    @jwt_required()
    def get(self, name):
        check=db.query.filter_by(name=name).first()
        if check:
            return {'name':check.name,'price':check.price}
        return {'item':None},404
    
    def put(self, name):
        # data=request.get_json()
        # parser=reqparse.RequestParser()
        # parser.add_argument('price', 
        #                     type=float,
        #                     required=True,
        #                     help=f'{"price"} is a required field')
        
        data=Item.parser.parse_args()
        check=db.query.filter_by(name=name)
        if check:
            check.price=data['price']
            db.session.add(check)
            db.session.commit()
            return {'name':check.name,'price':check.price}
        item=Item(name,data['price'])
        db.session.add(item)
        db.session.commit()
        return {'name':name,'price':data['price']},201
    
    def delete(self, name):
        # data=Item.parser.parse_args()
        
        check=db.query.filter_by(name=name)
        if check:
            db.session.delete(check)
            db.session.commit()
            return {name:'deleted'}
        return {'item':None},404
    
class Items(Resource,db):
    def get(self):
        rows_l=[]
        rows=db.query.all()
        for row in rows:
            rows_l.append({'name':row.name,'price':row.price})
        return {'items':rows_l}
    
    
    
    
    
    
    
    
    