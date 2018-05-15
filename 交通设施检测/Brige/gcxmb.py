#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @author: pengyangyan
 @contact: 531639577@qq.com
 @create time:2018-05-14 22:13
  
 """

from Brige import dbconnect

def insert(gcxmbm,gcxmmc):
    conn = dbconnect.dbConnect()
    cursor = conn.connect()
    sql = """insert into gcxmb(gcxmbm,gcxmmc) values(%s,%s)"""
    cursor.execute(sql,(gcxmbm,gcxmmc))
    conn.close()

def fetch():
    conn = dbconnect.dbConnect()
    cursor = conn.connect()
    sql =""" select * from gcxmb """
    cursor.execute(sql)
    result = cursor.fetchone()
    conn.close()
    return result
