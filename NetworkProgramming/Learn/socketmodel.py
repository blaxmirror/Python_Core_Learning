# socket()模块函数


from socket import socket
# 创建套接字语法 socket(socket_family, socket_type, protocol=0)


# 创建TCP/IP socket
tcpsocket = socket(socket.AF_INET, socket.SOCK_STREAM)
# 创建UDP/IP socket
udpsocket = socket(socket.AF_INET, socket.SOCK_DGRAM)
