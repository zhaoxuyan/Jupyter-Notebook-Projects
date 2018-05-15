#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @author: pengyangyan
 @contact: 531639577@qq.com
 @create time:2018-05-14 20:06
  
 """
PY_MYSQL_CONN_DICT = {
    "host": '202.202.243.33',
    "port": 3306,
    "user": 'bridge',
    "passwd": '123456',
    "db": '现场终端数据',
    "charset": 'utf8'
}
import pymysql
class dbConnect:
    def __init__(self):
        self.conn = None
        self.cursor = None
        self.__conn_dict = PY_MYSQL_CONN_DICT

    def connect(self, cursor=pymysql.cursors.DictCursor):
        try:
            self.conn = pymysql.connect(**self.__conn_dict)
            self.cursor = self.conn.cursor(cursor=cursor)
            return self.cursor
        except Exception as e:
            print("连接失败:%s"%e)

    def close(self):
        self.conn.commit()
        self.cursor.close()
        self.conn.close()



