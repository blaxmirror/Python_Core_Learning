#!/usr/bin/env python3

"""
创建tcp客户端伪码：
cs = socket()
cs.connect()
comm_loop:
    cs.send()/cs.recv()
cs.close()
"""

from socket import *

# HOST和PORT变量指服务器的主机名与端口号
HOST = 'localhost'  # or '127.0.0.1'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)

while True:
    data = input('> ')
    if not data:
        break
    tcpCliSock.send(bytes(data, 'utf-8'))
    data = tcpCliSock.recv(BUFSIZ)
    if not data:
        break
    print(data.decode('utf-8'))

tcpCliSock.close()
