#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
用于正则表达式练习的数据生成器 p34
"""

__author__ = 'Alex Ryan'

from random import randrange, choice
from string import ascii_lowercase as lc
from sys import maxsize  # 书中原是用来设定一个范围值，但由于在64位系统中，该maxsize实际为 2^63-1，不能使用
from time import ctime

# 设定一个高级域名的tuple用于选择
tlds = ('com', 'edu', 'net', 'org', 'gov')

for i in range(randrange(5, 11)):
    dtint = randrange(2**31-1)  # 随机生成一个时间数（自epoch以来的秒数）
    dtstr = ctime(dtint)  # 将时间转换为str
    llen = randrange(4, 8)  # 随机生成login的长度，4-8
    login = ''.join(choice(lc) for j in range(llen))  # 随机生成一个login字符串
    dlen = randrange(llen, 13)  # 随机生成域名的长度，llen-13
    dom = ''.join(choice(lc) for j in range(dlen))  # 随机生成一个dom字符串
    print('%s::%s@%s.%s::%d-%d-%d' % (dtstr, login, dom, choice(tlds), dtint, llen, dlen))
