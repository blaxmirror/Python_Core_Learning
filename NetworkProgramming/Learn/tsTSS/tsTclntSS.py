#!/usr/bin/env python3

from socket import *

HOST = 'localhost'  # or '127.0.0.1'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

while True:
    tcpCliSock = socket(AF_INET, SOCK_STREAM)
    tcpCliSock.connect(ADDR)
    data = input('> ')
    if not data:
        break
    tcpCliSock.send(b'%s\n' % bytes(data, 'utf-8'))
    data = tcpCliSock.recv(BUFSIZ)
    if not data:
        break
    print(data.strip().decode('utf-8'))
    tcpCliSock.close()