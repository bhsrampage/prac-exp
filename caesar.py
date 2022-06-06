pt = input("Enter Plain Text:- ")
key = int(input("Enter key:- "))
ct = ""

for i in pt:
    if i.isupper():
        ct+=chr((ord(i)-65 + key)%26 + 65)
    else:
        ct+=chr((ord(i)-97 + key)%26 + 97)

print(ct)
