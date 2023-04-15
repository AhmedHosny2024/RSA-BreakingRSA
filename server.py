from func import *
import socket
import json

#--------------------------------------------------------------
# initialize the socket 
#--------------------------------------------------------------
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = socket.gethostname()
port = 1234
s.bind(("127.0.0.1",port))

s.listen(1)
con,addr = s.accept()
print("got connection from ",addr)


#--------------------------------------------------------------
# Read the values of P , Q from a file or generate them randomly
#--------------------------------------------------------------
size = input("enter key size in bits : ")
size=int(size)
p,q=generate_prime(size//2)
n,phi=calcN(p,q)
e =calcE(phi)
d=modInv(e,phi)
#--------------------------------------------------------------
# send the public key of the reciever
#--------------------------------------------------------------
public_key=[e , n]

keys_list = json.dumps(public_key)
con.send(keys_list.encode())

while True:
    # try:
        C = con.recv(1024)
        Cipher = int(C.decode())
        decrypted = Decrypt([Cipher],n,d)
        for i in range(len(decrypted)):
            print(decrypted[i])
        con.send("d".encode()) 
    # except:
    #     con.close()
        

        
     
      