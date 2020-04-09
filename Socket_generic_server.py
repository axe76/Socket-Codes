# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 18:04:31 2019

@author: ACER
"""

import socket
import sys

def create_socket():
    try: 
        global host
        global port
        global s
        host = ""
        port = 9999
        s = socket.socket()
        print("Socket created")

    except socket.error as msg:
        print("Socket creation error:"+str(msg))
    
def bind_socket():
    try:
        global host
        global port
        global s
        s.bind(host,port)
        print("Socket binded to %s",port)
        s.listen(5)
        print("Socket is listening")
    except socket.error as msg:
        print("Socket binding error:"+str(msg))

def connect_socket():
        conn,address = s.accept()
        print("Connection with: IP-"+address[0]+" Port-"+address[1])
        send_msg(conn)
        conn.close()

def send_msg(conn):
    while True:
        cmd = input()
        if cmd == "quit":
            conn.close()
            s.close()
            sys.exit()
            
        if len(str.encode(cmd))>0:
            conn.send(str.encode(cmd))
            client_msg = str(conn.recv(1024),"utf-8")
            print("Client message = "+client_msg, end = "")

def main():
    create_socket()
    bind_socket()
    connect_socket()


    
        