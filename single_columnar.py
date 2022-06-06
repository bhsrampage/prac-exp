pt = input("Enter Plain Text:- ")
key = input("Enter key:- ")
l_key = list(key)
ct = ""
mat = [l_key]
l_key = sorted(l_key)

n = len(key)
temp = []
for i in pt:
    if len(temp) == n: 
        mat.append(temp)
        temp = []
    temp.append(i)

while len(temp) != n: temp.append('X')
mat.append(temp)

for i in l_key:
    for j in [row[mat[0].index(i)] for row in mat][1:]:
        ct+=j

print(ct)

