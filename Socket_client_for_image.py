# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 22:16:41 2019

@author: ACER
"""

import socket
import sys
import pickle
from PIL import Image
import numpy as np


myfile = open(r"C:\Users\ACER\Desktop\AI\DATASET\TEST\O\O_13192.jpg",'rb')
byt = myfile.read()
#pix = np.array(img)
#file = open('data.pkl', 'wb') 
#msg = pickle.dumps(pix)

#byt = bytes(msg)

s = socket.socket()
port = 9999
#s.connect(("172.17.10.67",port))
s.connect(("192.168.1.10",port))
#while True:
server_msg = str(s.recv(1024),"utf-8")
print("Server message = "+str(server_msg))
    #client_msg = input()
    #if server_msg == "Send image":
s.send(byt)
print("Hello")
'''else:
        s.send(str.encode(client_msg))'''
