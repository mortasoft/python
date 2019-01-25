#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
import socket

sock = socket.socket()
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(("localhost", 9199))

sock.listen(1)

sc, addr = sock.accept()

while True:
    recibido = sc.recv(1024)
    if recibido == "quit":
        break
    print("Recibido:",recibido.decode('utf-8'))
    sc.send(recibido)

print("Adios")
sc.close()
sock.close()


