#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @author: pengyangyan
 @contact: 531639577@qq.com
 @create time:2018-05-14 22:13
  
 """
from Brige import dbconnect
def fetchone():
    conn = dbconnect.dbConnect()
    cousor = conn.connect()
    sql ="""SELECT  gcxmbm cdbm, cdmc, cgqbm, jldw, sfqy, sjlx, sflb, lbfs, lbcs, bz FROM cdb WHERE 1 """
    cousor.execute(sql)
    result = cousor.fetchone()
    conn.close()
    return result

def insert(**kwargs):
    conn = dbconnect.dbConnect()
    cursor = conn.connect()
    sql = """insert into cdb(%s) values(%s)"""
    key_list = []
    value_list = []
    for k, v in kwargs.items():
        key_list.append(k)
        value_list.append('%%(%s)s' % k)
    sql = sql % (','.join(key_list), ','.join(value_list))
    cursor.execute(sql, kwargs)
    conn.close()
