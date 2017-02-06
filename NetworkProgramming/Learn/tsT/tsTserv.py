#!/usr/bin/env python3

"""
创建tcp服务器伪码：
ss = socket()
ss.bind()
ss.listen()
inf_loop:
    cs = ss.accept()
    comm_loop:
        cs.recv()/cs.send()
    cs.close()
ss.close()
"""

from socket import *
from time import ctime

# HOST变量是空白的，这是对bind()方法的标识，表示可以使用任何可用的地址
HOST = ''
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
# listen方法的参数是连接被转接或拒绝前，传入连接请求的最大数
tcpSerSock.listen(5)

while True:
    print('waiting for connection...')
    # accept方法返回一个客户端套接字和客户端的地址
    tcpCliSock, addr = tcpSerSock.accept()
    print('...connected from:', addr)

    while True:
        data = tcpCliSock.recv(BUFSIZ)
        if not data:
            break
        tcpCliSock.send(b'[%s] %s' % (bytes(ctime(), 'utf-8'), data))

    tcpCliSock.close()
tcpSerSock.close()
