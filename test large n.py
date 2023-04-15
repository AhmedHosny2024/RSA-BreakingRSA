from func import *
import time
import matplotlib.pyplot as plt

key_size=[]

m="1"
encrypt_time=[]
for j in range(30,400):
    p,q=generate_prime(j//2)
    n , phi =calcN(p,q)
    e=calcE(phi)
    start = time.time()
    cipher_text= Encrypt(m,n,e)   
    end = time.time()
    encrypt_time.append(end-start)
    key_size.append(j)
plt.xlabel('key size')
plt.ylabel('time to encrypt')
plt.title('relation between time to encryption & size of key')
plt.plot(key_size, encrypt_time, 'b')
plt.show()


decrypt_time=[]
cipher_text=[1]
for j in range(30,400):
    p,q=generate_prime(j//2)
    n , phi =calcN(p,q)
    e=calcE(phi)
    start = time.time()
    m= Decrypt(cipher_text,n,e)   
    end = time.time()
    decrypt_time.append(end-start)
    # key_size.append(j)
plt.xlabel('key size')
plt.ylabel('time to decrypt')
plt.title('relation between time to decryption & size of key')
plt.plot(key_size, decrypt_time, 'b')
plt.show()


attack_time=[]
cipher_text=[1]

for j in range(10,50):
    p,q=generate_prime(j//2)
    n , phi =calcN(p,q)
    e=calcE(phi)
    d=modInv(e,phi)
    start = time.time()
    PR= mathematical_attack(e,n)   
    end = time.time()
    key_size.append(j)
    if(d!=PR):
        print(50*'#')
        print("/n")
    attack_time.append(end-start)
plt.xlabel('key size')
plt.ylabel('time to decrypt')
plt.title('relation between time to attack time & size of key')
plt.plot(key_size, attack_time, 'b')
plt.show()