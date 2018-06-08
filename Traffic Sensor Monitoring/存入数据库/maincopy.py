#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @author: pengyangyan
 @contact: 531639577@qq.com
 @create time:2018-04-17 23:30

 """
import socket
import codecs
import time
import datetime
from Brige import crc16
import struct
from Brige import cdsjb,cdb,gcxmb

"""
client
    connect()
    recv()
    send()
    sendall()

"""
def main():
    sk = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print(sk)
    address = ('10.1.156.82', 8001)
    sk.connect(address)
    inp = '030300000002c5e9'
    gcxmbm, gcxmmc = "631507030103彭阳宴", "温湿度处理"
    cdbm1, cdbm2 = "shidu", "wendu"
    cdmc1, cdmc2 = "湿度", "温度"
    while True:
        total_wendu,total_shidu=0,0
        list_wendu = []
        list_shidu = []
        global inst_wendu
        global inst_shidu
        global avg_wendu
        global avg_shidu
        global max_wendu
        global max_shidu
        global min_wendu
        global min_shidu
        n =0
        begin_time = time.time()
        while True:
            sk.send(codecs.decode(inp, 'hex'))
            try:
                result = sk.recv(1024)
            except socket.timeout:
                print('timeout')
            crc=crc16.crc16(result[:-2])
            if crc==result[-2:]:
                print('CRC16成功')
            shidu,wendu=struct.unpack('>hh',result[3:7])
            shidu/=100
            wendu/=100
            #比较上一次的温湿度的波动
            with open("last_data",'r') as r:
                last_data =  r.read()
            if not last_data:
                last_data = str(wendu)+'%'+str(shidu)
            last_wendu,last_shidu = last_data.split("%")
            last_wendu,last_shidu = float(last_wendu),float(last_shidu)
            if(abs(shidu-last_shidu)>5 or abs(wendu-last_wendu>5)):
                print(abs(shidu-last_shidu),abs(wendu-last_wendu))
                print("数字波动太大，未记录")
                continue
            else:
                # 将当前温度湿度写入文档作为记录
                data = str(wendu) + "%" + str(shidu)
                with open("last_data", 'w') as f:
                    f.write(data)
                n += 1
                list_shidu.append(shidu)
                list_wendu.append(wendu)
                total_wendu += wendu
                total_shidu +=shidu
                end_time = time.time()
                if(end_time-begin_time>5):
                    inst_wendu = list_wendu[-1]
                    inst_shidu = list_shidu[-1]
                    list_wendu.sort()
                    list_shidu.sort()
                    avg_wendu = total_wendu/n
                    avg_shidu = total_shidu/n
                    max_wendu = list_wendu[-1]
                    max_shidu = list_shidu[-1]
                    min_wendu = list_wendu[0]
                    min_shidu = list_shidu[0]
                    print("最大温度%s，最小温度%s，平均温度%s，瞬时温度%s" % (max_wendu, min_wendu, avg_wendu, inst_wendu))
                    print("最大湿度%s，最小湿度%s，平均湿度%s，瞬时湿度%s" % (max_wendu, min_wendu, avg_wendu, inst_wendu))
                    time.sleep(0.1)
                    break
                else:
                    continue
        cur_time = datetime.datetime.now()
        print("最大温度%s，最小温度%s，平均温度%s，瞬时温度%s" %(max_wendu,min_wendu,avg_wendu,inst_wendu),cur_time)
        print("最大湿度%s，最小湿度%s，平均湿度%s，瞬时湿度%s" % (max_wendu, min_wendu, avg_wendu, inst_wendu),cur_time)
        print("开始向数据库传入数据...")
        gcxmb_data = gcxmb.fetch()
        if not gcxmb_data:
            try:
                gcxmb.insert(gcxmbm,gcxmmc)
            except Exception:
                print("工程项目表插入失败")
        cdb_data = cdb.fetchone()
        if not cdb_data:
            try:
                cdb.insert(gcxmbm=gcxmbm,cdbm=cdbm1,cdmc=cdmc1,cgqbm="03",jldw="RH",sflb=1)
                cdb.insert(gcxmbm=gcxmbm, cdbm=cdbm2, cdmc=cdmc2, cgqbm="03", jldw="摄氏度", sflb=1)
            except Exception:
                print("测点表插入失败 ")
        try:
            cdsjb.insert(gcxmbm=gcxmbm,cdbm=cdbm1,clsj=cur_time,avg=avg_shidu,max=max_shidu,min=min_shidu,inst=inst_shidu)
            cdsjb.insert(gcxmbm=gcxmbm, cdbm=cdbm2, clsj=cur_time,avg=avg_wendu,max=max_wendu,min=min_wendu,inst=inst_wendu)
            print("传入成功")
        except:
            print("测点数据表插入失败")
    sk.close()
main()
