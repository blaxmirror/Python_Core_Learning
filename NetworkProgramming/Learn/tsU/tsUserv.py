#!/usr/bin/env python3

"""
创建UDP服务器伪码：
ss = socket()
ss.bind()
inf_loop:
    cs = ss.recvfrom()/ss.sendto()
ss.close()
"""

from socket import *
from time import ctime

HOST = ''
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)


udpSerSock = socket(AF_INET, SOCK_DGRAM)
udpSerSock.bind(ADDR)

while True:
    print('waiting for message...')
    data, addr = udpSerSock.recvfrom(BUFSIZ)
    udpSerSock.sendto(b'[%s] %s' % (bytes(ctime(), 'utf-8'), data), addr)
    print('...received from and returned to:', addr)

udpSerSock.close()
