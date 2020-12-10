#!/usr/bin/python
# -*- coding: UTF-8 -*-

import socket
import os

def echo_client():
    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    host = "localhost"
    print(host)
    port = 10002
    client.connect((host,port))
    print(client)
    while True:
        fileName = input('input fileName > ')
        try:
            with open(fileName,'r') as f:
                client.sendfile(f)
                for line in f.readlines():
                    #发送到服务端
                    client.sendall(line.encode())
        except FileNotFoundError as fe:
            print('FileNotFoundError')
            print(fe)            
        #接收服务端数据
        data = client.recv(1024)
        if not data:
            break
        else:
            print(data.decode('utf-8'))
    client.close()

if __name__ == "__main__":
    echo_client()