import numpy as np

pt = input("Enter Plain Text:- ")
key = input("Enter key:- ")
ct = ""
key_mat = []
pt_mat = []
temp = []
for i in pt:
    temp.append(ord(i)-65)
pt_mat.append(temp)
print(pt_mat)
k = 0
for i in range(3):
    temp = []
    for j in range(3):
        temp.append(ord(key[k])-65)
        k+=1
    key_mat.append(temp)
print(key_mat)
ct_mat = np.matmul(key_mat,np.transpose(pt_mat))

print(ct_mat)
for i in ct_mat.flatten(): ct+=chr(i%26 + 65)

print("Cipher Text:- " + ct)
