# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 22:24:53 2020

@author: Kartik Saini
"""

from user import User
# from werkzeug,security import safe_str_cmp

# users=[
#       {
#         'id':1,
#         'username':'kartik',
#         'password':'abcd'
#         }
#       ]

# username_mapping=[
#     {
#     'kartik':{
#         'id':1,
#         'username':'kartik',
#         'password':'abcd'
#         }
#     }
#     ]

# userid_mapping=[
#     {
#     '1':{
#         'id':1,
#         'username':'kartik',
#         'password':'abcd'
#         }
#     }
#     ]

users=[
        User(1001,'kartik','abcd')   #id can be string also
        ]

username_mapping={u.username : u for u in users}

userid_mapping={u.id : u for u in users}

# def authenticate(userna,passw):           #this will also run with no error.
#     user=username_mapping.get(userna,None)
#     if user and user.password==passw:
#         return user

def authenticate(username,password):
    user=username_mapping.get(username,None)
    if user and user.password==password:
        return user

def identity(payload):
    userid=userid_mapping.get(payload['identity'],None)
    return userid


    













