#!/usr/bin/env python3

"""
创建UDP客户端伪码：
cs = socket()
comm_loop():
    cs.sendto()/cs.recvfrom()
cs.close()
"""

from socket import *

HOST = 'localhost'  # or '127.0.0.1'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

udpCliSock = socket(AF_INET, SOCK_DGRAM)

while True:
    data = input('> ')
    if not data:
        break
    udpCliSock.sendto(bytes(data, 'utf-8'), ADDR)
    data, ADDR = udpCliSock.recvfrom(BUFSIZ)
    if not data:
        break
    print (data.decode('utf-8'))

udpCliSock.close()