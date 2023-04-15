import random
import math
import Crypto
from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import AES

def prime(num): 
    return (num > 1 and all(num % i for i in range(2,int(math.sqrt(num))+1)))


def generate_prime(N):
    p=Crypto.Util.number.getPrime(N)
    q=Crypto.Util.number.getPrime(N)
    # p = random.randint(beg, end)
    # q = random.randint(beg, end)
    # while not prime(p):
        # p = random.randint(beg, end)
    # while not prime(q) or p == q:
        # q = random.randint(beg, end)
    while(p==q):
        q=Crypto.Util.number.getPrime(N)
    return p , q 
def calcN(p,q):
    n=p*q
    phi=(p-1)*(q-1)
    return n , phi

def modExp(a, n, mod):
   if n == 0:     return 1 % mod
   elif n == 1:   return a % mod
   else:
      b = modExp(a, n // 2, mod)
      b = b * b % mod
      if n % 2 == 0:
         return b
      else:
         return b * a % mod
      
def ExtendedEuclid(a, b):
    if b == 0:
        return (1, 0)
    (x, y) = ExtendedEuclid(b, a % b)
    k = a // b
    return (y, x - k * y)

def modInv(e, phi):
    (b, x) = ExtendedEuclid(e, phi)
    if b < 0:
        b = (b % phi + phi) % phi # as we don't want -ve integers
    return b
# print(modInv(5,12))

def GCD(a, b):
   return a if b == 0 else  GCD(b, a % b)


def calcE(phi):
    r=random.randint(0,phi)
    while(GCD(r,phi)!=1 and r>1):
        r=random.randint(0,phi)
    return r

data=['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ']
def strToInt(message_str):
   res = 0
   j=(len(message_str))-1
   for i in range(len(message_str)):
        if(message_str[i] in data ):
            res += data.index(str(message_str[i])) * (37**j)
        else:
            res = 36 * (37**36)
        j=j-1
   return res

def converToInt(msg):
    msg=msg.lower()
    enc=[]
    add=(5 - (len(msg) % 5) )%5
    for i in range(0,add):
        msg=msg + ' '
    for i in range(0,len(msg),5):
        enc.append(strToInt(msg[i:i+5]))
    return enc
# print(converToInt('hi s7hi s7'))

def intToStr(n):
   res = ""
   while n > 0:
      res = data[n % 37] +res
      n //= 37
   return res
# print(intToStr(32822818))

def convertToStr(msg):
    dec=[]
    for i in range(0,len(msg)):
        dec.append(intToStr(msg[i]))
    return dec
x=[32822818, 32822818, 32822847]
# print(convertToStr(x))

def Encrypt (m, n, e):
   m = converToInt(m)
   while(max(m) > n):
            print("take care the other side cannot receive this message correctly as M > n which break RSA condition\n")
            print("please, reconsider and submit another message .. \n")
            m = input("type the message to be sent : > ")
            m = converToInt(m)  
   c = []
   for i in range(len(m)):
      c.append(modExp(m[i], e, n))
   return c

# print(Encrypt('hi s7', 21, 5))


def Decrypt(c, n, d):
   m=[]
   for i in range(len(c)):
      m.append(modExp(c[i], d, n))
   return convertToStr(m)
# print(Decrypt([7], 21, 5))

def factorize(n):
   if (n % 2) == 0:
      return [2] + factorize(n//2)
   
   integer = 3
   while integer <= (n**0.5):     
      if n % integer == 0:      
         return [integer] + factorize(n // integer)
      else:
         integer += 2                        # Since all primes are odd.
   return [n]

def mathematical_attack(e,n):
   factors = factorize(n)
   if(len(factors) == 2):
    d=modInv(e,(factors[0]-1)*(factors[1]-1))
    return d
   else: 
    return "NOT RSA" 
# print(mathematical_attack(5,21))