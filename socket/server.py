# coding=utf-8
from socket import *
from time import ctime

addr = ('127.0.0.1', 9888)
sersocket = socket(AF_INET, SOCK_STREAM)
sersocket.bind(addr)
sersocket.listen(1)
while True:
    print "waiting for cli connect ..."
    tcpsocket, add = sersocket.accept()  # accept函数返回一个socket对象和一个客户端地址
    print "the client addr is :", add
    while True:
        data = tcpsocket.recv(1024)
        if not data:
            break
        tcpsocket.send('[%s] | %s' % (ctime(), data))
