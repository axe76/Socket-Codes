# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 18:04:31 2019

@author: ACER
"""

import socket
from PIL import Image
import sys
import pickle

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
        s.bind((host,port))
        print("Socket binded to %s",port)
        s.listen(5)
        print("Socket is listening")
    except socket.error as msg:
        print("Socket binding error:"+str(msg))

def connect_socket():
        conn,address = s.accept()
        print("Connection with: IP-"+str(address[0])+" Port-"+str(address[1]))
        send_msg(conn)
        conn.close()

def send_msg(conn):
    #data = b""
    cmd = input()
    if cmd == "quit":
        conn.close()
        s.close()
        #sys.exit()
    conn.send(str.encode(cmd))
    while True:
        #packet = conn.recv(40960000)
        '''if packet: 
            print("Received")           
            break'''
        myfile = open("image.jpg", 'wb')
        print('File created')
        #myfile.write(data)

        data = conn.recv(40960000)
        print('Received')
        if not data:
            myfile.close()
            conn.close()
            break
        myfile.write(data)
        print('Data written')
        myfile.close()
        i = Image.open("image.jpg")
        i.show()
        s.close()
        #data += packet
        
        
        '''if len(str.encode(cmd))>0:
            conn.send(str.encode(cmd))
            #data = conn.recv(40960000)
            client_msg = str(data)
            if client_msg.startswith("Chat"):
                print("Client message = "+client_msg, end = "")
                send_msg(conn)
            elif data:    
            #myfile = open("Image.jpg",'wb')
            #print("File opened")
            #myfile.write(data)
            #data = conn.recv(40960000)
            packet = conn.recv(4096)
            if not packet: break
            data += packet
            print("Received")
            #myfile.write(img)
            #print("File written")
            #myfile.close()
            #print("File closed")
            #img = Image.open(myfile)'''
    '''print('Saz')
    img = pickle.loads(packet)
    print('Hi')
    fin_img = Image.fromarray(img)
    print('Hi1')
    Image.show(fin_img)
    print('Hi2')'''
                

def main():
    create_socket()
    bind_socket()
    connect_socket()
    
main()


    
        