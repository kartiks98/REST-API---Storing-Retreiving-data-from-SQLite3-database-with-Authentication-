# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 02:03:45 2020

@author: Kartik Saini
"""

import sqlite3

connection=sqlite3.connect('MyData.db')
cursor=connection.cursor()
        
query='create table if not exists users(id integer primary key, username text, password text)'

cursor.execute(query)

query_item_table='create table if not exists items(name text, price real)'

cursor.execute(query_item_table)

cursor.execute('insert into items values("test",10.79)')

connection.commit()

connection.close()