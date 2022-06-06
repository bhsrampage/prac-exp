
from Crypto.Cipher import AES
from random import randint

def o1() :
    msg = input("Enter message: ")

    key = []
    for i in range(16) :
        key.append(randint(0,255))
    key = bytes(key)

    cipher = AES.new(key, AES.MODE_EAX)
    nonce = cipher.nonce

    ct, _ = cipher.encrypt_and_digest(bytes(msg, 'ascii'))
    print(f"Encrypted: {ct}")

    pt = AES.new(key, AES.MODE_EAX, nonce=nonce).decrypt(ct)
    print(f"Decrypted: {pt}")

def o2() :
    file = open("data.txt")
    data = bytes(file.readlines()[0], "ascii")
    file.close()

    key = []
    for i in range(16) :
        key.append(randint(0,255))
    key = bytes(key)

    cipher = AES.new(key, AES.MODE_EAX)
    nonce = cipher.nonce

    ct, _ = cipher.encrypt_and_digest(data)
    print(f"Encrypted: {ct}")

    pt = AES.new(key, AES.MODE_EAX, nonce=nonce).decrypt(ct)
    print(f"Decrypted: {pt}")

o1()