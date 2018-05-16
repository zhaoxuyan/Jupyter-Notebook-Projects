#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @author: pengyangyan
 @contact: 531639577@qq.com
 @create time:2018-05-14 20:31
  
 """
from Brige import dbconnect

def fetch():
    conn = dbconnect.dbConnect()
    cursor = conn.connect()
    cursor.execute("select * from cdsjb")
    result = cursor.fetchall()
    conn.close()
    print("success")
    return result
def insert(**kwargs):
    conn = dbconnect.dbConnect()
    cursor =conn.connect()
    sql = """insert into cdsjb(%s) values(%s)"""
    key_list = []
    value_list = []
    for k, v in kwargs.items():
        key_list.append(k)
        value_list.append('%%(%s)s' % k)
    sql = sql % (','.join(key_list), ','.join(value_list))
    cursor.execute(sql, kwargs)
    conn.close()






