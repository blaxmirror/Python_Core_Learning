#!/usr/bin/env python3

from twisted.internet import protocol, reactor

HOST = 'localhost'
PORT = 21568


class TSClntProtocol(protocol.Protocol):
    # 添加方法sendData，在建立连接和收到数据时调用
    def sendData(self):
        data = input('> ')
        # data存在则传输，否则关闭连接
        if data:
            print('...sending %s...' % data)
            self.transport.write(data.encode('utf-8'))
        else:
            self.transport.loseConnection()

    # 一旦建立连接，就发送数据
    def connectionMade(self):
        self.sendData()

    # 一旦接受到数据，则打印data，并继续执行sendData
    def dataReceived(self, data):
        print(data.decode('utf-8'))
        self.sendData()


# 创建客户端工厂，创建一个到服务器的连接并运行reactor
class TSClntFactory(protocol.ClientFactory):
    protocol = TSClntProtocol
    clientConnectionLost = clientConnectionFailed = \
        lambda self, connector, reason: reactor.stop()

reactor.connectTCP(HOST, PORT, TSClntFactory())
reactor.run()
