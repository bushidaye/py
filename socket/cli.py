from socket import *

clisocket = socket(AF_INET, SOCK_STREAM)
clisocket.connect('192.168.20.100', '9888')
while True:
    data = raw_input('> ')
    if not data:
        break
    clisocket.send(data)
    data = clisocket.recv(10)
    if not data:
        break
    print data
clisocket.close()
