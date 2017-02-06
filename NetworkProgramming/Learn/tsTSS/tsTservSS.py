#!/usr/bin/env python3

from socketserver import (TCPServer as TCP,
                          StreamRequestHandler as SRH)
from time import ctime

HOST = ''
PORT = 21567
ADDR = (HOST, PORT)


class MyRequestHandler(SRH):
    # 重写handle方法
    def handle(self):
        print('...connected from:', self.client_address)
        # 使用readline来获取客户端消息，使用write来送回消息
        self.wfile.write(b'[%s] %s' % (bytes(ctime(), 'utf-8'), self.rfile.readline()))

# 创建TCP服务器
tcpServ = TCP(ADDR, MyRequestHandler)
print('waiting for connection...')
tcpServ.serve_forever()
