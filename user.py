# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 22:42:57 2020

@author: Kartik Saini
"""


from flask_restful import Resource,reqparse
from db import db

class User(db.Model):
    __tablename__='users'
    
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(80))
    password=db.Column(db.String(80))
    
    def __init__(self,username,password):
        self.username=username
        self.password=password
        
    @classmethod
    def find_by_username(cls,username):
       return cls.query.filter_by(username=username).first()
        
    @classmethod
    def find_by_id(cls,_id):
        return cls.query.filter_by(id=_id).first()
        
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
        
        if User.find_by_username(data['username']):
            return {f'{data["username"]}':'already exists'}, 400
        user=User(**data)
        db.session.add(user)
        db.session.commit()
    
        return {f'{data["username"]}':'added successfully'}, 201