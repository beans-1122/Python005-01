#!/usr/bin/python
# -*- coding: UTF-8 -*-
import socket
import time
import os

def echo_server():
    #AF_INET ipv4 SOCK_STREAM tcp
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    host = "localhost"
    port = 10002
    server.bind((host,port))
    #最大连接数量
    server.listen(1)
    while True:
        print('wating for connection...')
        c,addr = server.accept()
        print(f'Connected by {addr}')
        while True:
            data = c.recv(1024)
            if not data:
                break
            newFileName = 'savedFile'
            with open(newFileName,'w') as f:
                f.write(c.recv(1024).decode())
        c.close()
    server.close()

if __name__ == "__main__":
    echo_server()
    print(time.localtime())
    timestap = time.strftime("%Y-%m-%d",time.localtime())
    print(timestap)