#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @author: pengyangyan
 @contact: 531639577@qq.com
 @create time:2018-05-08 16:46
  
 """
def crc16(x):
    u'''
    @summary: 计算CRC16值
    @param x: bytes
    @return: 返回2字节值，类似：b'\x7B\x2A'。
    '''
    if not isinstance(x, bytes):
        raise ValueError('Parameter must be a bytes type')
    b = 0xA001
    a = 0xFFFF
    for byte in x:
        a = a ^ byte
        for _ in range(8):
            last = a % 2
            a = a >> 1
            if last == 1:
                a = a ^ b
    aa = '0' * (6 - len(hex(a))) + hex(a)[2:]
    ll, hh = int(aa[:2], 16), int(aa[2:], 16)
    rtn = '%x' % (hh * 256 + ll & 0xffff)
    while len(rtn) < 4:
        rtn = '0' + rtn
    rtn = hextobytes(rtn)
    return rtn
def hextobytes(x):
    if not isinstance(x, str):
        x = str(x, 'ascii')
    return bytes.fromhex(x)
def bytestohex(x):
    if not isinstance(x, bytes):
        x = bytes(x, 'ascii')
    return ''.join(["%02x" % i for i in x]).strip()


