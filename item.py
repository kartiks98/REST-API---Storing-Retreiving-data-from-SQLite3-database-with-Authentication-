# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 17:49:51 2020

@author: Kartik Saini
"""

from flask_restful import Resource,reqparse
from flask_jwt import jwt_required
import sqlite3

class Item(Resource):
    parser=reqparse.RequestParser()
    parser.add_argument('price', 
                            type=float,
                            required=True,
                            help=f'{"price"} is a required field')
    
    def post(self, name):
        data=Item.parser.parse_args()
        connection=sqlite3.connect('MyData.db')
        cursor=connection.cursor()
        select=cursor.execute('select * from items where name=?',(name,))
        row=select.fetchone()
        if row:
            return {f'{name}':'already exists'},400
        cursor.execute('insert into items values(?,?)',(name,data['price']))
        connection.commit()
        connection.close()
        return {'name':name,'price':data['price']},201
        
    
    @jwt_required()
    def get(self, name):
        connection=sqlite3.connect('MyData.db')
        cursor=connection.cursor()
        select=cursor.execute('select * from items where name=?',(name,))
        row=select.fetchone()
        if row:
            return {'name':row[0],'price':row[1]}
        return {'item':None},404
    
    def put(self, name):
        # data=request.get_json()
        # parser=reqparse.RequestParser()
        # parser.add_argument('price', 
        #                     type=float,
        #                     required=True,
        #                     help=f'{"price"} is a required field')
        
        data=Item.parser.parse_args()
        connection=sqlite3.connect('MyData.db')
        cursor=connection.cursor()
        select=cursor.execute('select * from items where name=?',(name,))
        row=select.fetchone()
        updated_item={'name':name,'price':data['price']}
        if row:
            cursor.execute('update items set price=? where name=?',
                                  (updated_item['price'],updated_item['name']))
            connection.commit()
            connection.close()
            return updated_item
        cursor.execute('insert into items values(?,?)',(name,data['price']))
        connection.commit()
        connection.close()
        return updated_item,201
    
    def delete(self, name):
        # data=Item.parser.parse_args()
        connection=sqlite3.connect('MyData.db')
        cursor=connection.cursor()
        select=cursor.execute('select * from items where name=?',(name,))
        row=select.fetchone()
        if row:
            cursor.execute('delete from items where name=?',(name,))
            connection.commit()
            connection.close()
            return {name:'deleted'}
        connection.commit()
        connection.close()
        return {'item':None},404
    
class Items(Resource):
    def get(self):
        connection=sqlite3.connect('MyData.db')
        cursor=connection.cursor()
        select_all=cursor.execute('select * from items')
        rows=select_all.fetchall()
        rows_l=[]
        for row in rows:
            rows_l.append({'name':row[0],'price':row[1]})
        return {'items':rows_l}
    
    
    
    
    
    
    
    
    