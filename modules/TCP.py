#!/usr/bin/python           # This is client.py file

import socket
import modules.setup as setup

def setupServer():
    s = socket.socket()
    s.bind((setup.host, setup.port))
    s.listen(setup.maxConnections)

    return s

def setupClient():
    s = socket.socket()         # Create a socket object
    s.connect((setup.host, setup.port))

    return s

def sendIFrame():
    pass
