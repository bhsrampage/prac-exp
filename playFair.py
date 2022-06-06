pt = input("Enter Plain Text:- ")
key = input("Enter key:- ")
ct = ""
play_fair = []

def find(matrix , element):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == element: return (i,j)
def contains(i):
    if i in play_fair:
        return True
    if i=="I" and "J" in play_fair:
        print("j present")
        return True
    if i=="J" and "I" in play_fair:
        print("i present")
        return True

    return False

for i in key:
    if not contains(i): play_fair.append(i)

for i in range(26):
    curr = chr(i+65)
    if not contains(curr): play_fair.append(curr)

print(play_fair)
mat = []
k = 0
for i in range(5):
    temp = []
    for j in range(5):
        temp.append(play_fair[k])
        k+=1
    mat.append(temp)

print(mat)
for i in range(0,len(pt)-1,2):
    (row1,col1) = find(mat,pt[i])
    (row2,col2) = find(mat,pt[i+1])

    if(row1 == row2):
        if col1 < col2:
            ct+= mat[row1][(col1+1)%5] + mat[row2][(col2+1)%5]
        else: ct+= mat[row1][(col2+1)%5] + mat[row2][(col1+1)%5]
    
    elif(col1 == col2):
        if row1 < row2:
            ct+= mat[(row1+1)%5][col1] + mat[(row2+1)%5][col1]
        
        else: ct+= mat[(row2+1)%5][col1] + mat[(row1+1)%5][col1]
    
    else: 
        ct+= mat[row1][col2] + mat[row2][col1]
    
print("Cipher Tex:- " + ct)
    

