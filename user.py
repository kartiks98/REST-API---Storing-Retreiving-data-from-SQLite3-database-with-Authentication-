# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 22:42:57 2020

@author: Kartik Saini
"""


import sqlite3
from flask_restful import Resource,reqparse

class User():
    def __init__(self,_id,username,password):
        self.id=_id
        self.username=username
        self.password=password
        
    # @classmethod
    def find_by_username(self,username):
        connection = sqlite3.connect('MyData.db')
        cursor = connection.cursor()
        
        select_query='select * from users where username=?'
        result=cursor.execute(select_query,[username,])
        row=result.fetchone()
        
        if row:
            user=User(*row)
            return user
        else:
            return None
        
    # @classmethod
    def find_by_id(self,_id):
        connection = sqlite3.connect('MyData.db')
        cursor = connection.cursor()
        
        select_query='select * from users where id=?'
        result=cursor.execute(select_query,[_id,])
        row=result.fetchone()
        
        if row:
            user=User(*row)
            return user
        else:
            return None
        
class UserReg(Resource):
    parser=reqparse.RequestParser()
    parser.add_argument('username', 
                        type=str,
                        required=True,
                        help='Please enter username')
    parser.add_argument('password', 
                        type=str,
                        required=True,
                        help='Please enter password')
    # data=UserReg.parser.parse_args()
    def post(self):
        # global data
        data=UserReg.parser.parse_args()
        
        if User.find_by_username(None,data['username']):
            return {f'{data["username"]}':'already exists'}, 400
        
        
        connection=sqlite3.connect('MyData.db')
        cursor=connection.cursor()
        
        # select_query='select * from users'
        # result=cursor.execute(select_query)
        # rows=result.fetchall()
        
        # for row in rows:
        #     if row[1] == data['username']:
        #         return {f'{data["username"]}':'already exists'}, 400
        
        
        # """The below statement will work but not recommended beause of SQL injection attack."""
        
        # query=f'insert into users values(null,"{data["username"]}","{data["password"]}")'
        # cursor.execute(query)
        
        
        # """The below statement will not work"""
        
        # query=f'insert into users values(null,{data["username"]},{data["password"]})'
        # cursor.execute(query)        
        
        query='insert into users values(null,?,?)'
        cursor.execute(query,(data['username'],data['password']))
        
        connection.commit()
        connection.close()
    
        return {f'{data["username"]}':'added successfully'}, 201