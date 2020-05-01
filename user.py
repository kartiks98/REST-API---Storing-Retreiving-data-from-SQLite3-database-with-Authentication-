# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 22:42:57 2020

@author: Kartik Saini
"""


class User():
    def __init__(self,_id,username,password):
        self.id=_id
        self.username=username
        self.password=password
        
# class User():
#     def __init__(self,_id,username,password):
#         self.id=_id
#         # self.username=username              #this will run with no error
#         self.password=password                #but with wrong logic.