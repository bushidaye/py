from time import ctime

from socket import *

SerSocket = socket(AF_INET, SOCK_STREAM)
SerSocket.bind('192.168.20.100', '9888')
SerSocket.listen(2)

while True:
    print 'Server is starting listen ...'
    tcpclisock, addr = SerSocket.accept()
    print "connect from ", addr

    while True:
        data = tcpclisock.recv(10)
        if not data:
            break
        tcpclisock.send('[%s] ，%s' % (ctime(), data))
        tcpclisock.close()
SerSocket.close()