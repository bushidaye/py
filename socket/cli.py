from socket import *

add = ('127.0.0.1', 9888)
clisocket = socket(AF_INET, SOCK_STREAM)
clisocket.connect(add)
while True:
    data = raw_input('> ')
    if not data:
        break
    clisocket.send(data)
    data = clisocket.recv(1024)
    if not data:
        break
    print data
clisocket.close()
