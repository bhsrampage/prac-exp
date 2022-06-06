from operator import mod

p = 13
q = 2
e = 2
n = p*q #take same as bounding value

fi = (p-1)*(q-1)

def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)

while(gcd(fi,e) != 1):
    e+=1

i = 1

while((fi*i +1)%e != 0):
    i+=1

d = (fi*i +1)//e

private_key = (d,n)
public_key = (e,n)

print(private_key)
print(public_key)
def encrypt(pt):
    return mod(pow(ord(pt)-65,public_key[0]),public_key[1])

def decrypt(ct):
    return mod(pow(ord(ct)-65,private_key[0]),private_key[1])

ct = "".join([chr(encrypt(i) + 65) for i in "HELLO"])
print(ct)
pt = "".join([chr(decrypt(i) + 65) for i in ct])
print(ct,pt)
