#!/usr/bin/env python3

from twisted.internet import protocol, reactor
from time import ctime

PORT = 21568


class TSServProtocol(protocol.Protocol):
    # 当一个客户端连接到服务器时就会执行connectionMade()方法
    def connectionMade(self):
        clnt = self.clnt = self.transport.getPeer().host
        print('...connected from:', clnt)
    # 当服务器收到客户端发送的数据，就会调用dataReceived()方法
    def dataReceived(self, data):
        print('received data: %s' % data.decode('utf-8'))
        self.transport.write(b'[%s] %s' % (bytes(ctime(), 'utf-8'), data))

# 创建协议工厂（因为每次得到一个接入连接时都能"制造"协议的一个实例）
factory = protocol.Factory()
factory.protocol = TSServProtocol
print('waiting for connection...')
# 在reactor中安装一个TCP监听器，以此检查服务请求
# 收到一个请求时，就会创建一个TSServProtocol实例来处理请求
reactor.listenTCP(PORT, factory)
reactor.run()