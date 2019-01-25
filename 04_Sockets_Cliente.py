#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
import socket

socket = socket.socket()
socket.connect(("localhost",9199))

while True:
    mensaje = input("Digite un mensaje: ").encode('utf-8')
    socket.send(mensaje)
    if mensaje.decode('utf-8') == "quit":
        break

print("adios")

socket.close()