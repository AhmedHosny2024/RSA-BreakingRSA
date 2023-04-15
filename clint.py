import socket
import json
from func import *
import time

#--------------------------------------------------------------
# initialize the socket 
#--------------------------------------------------------------
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
port=1234  
s.connect(("127.0.0.1",port))

#--------------------------------------------------------------------
# Start the communication by receiving the public key from the sender
#--------------------------------------------------------------------

keys = s.recv(1024).decode()
keys = json.loads(keys)


e = keys[0]
n = keys[1]
    
#--------------------------------------------------------------
#     sending ....
#-------------------------------------------------------------- 

while True:
    # try:
        M = input("type the message to be sent : > ")
        cipher_text= Encrypt(M,n,e)   
        for i in range (len(cipher_text)):
            s.send(str(cipher_text[i]).encode())   
            C = s.recv(1024)
    # except:
    #     s.close() 