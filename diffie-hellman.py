from operator import mod

q = 11
alpha = 7

class Entity:
    def __init__(self,k):
        self.private_key = k
    
    def generate_y(self):
        return mod(pow(alpha,self.private_key),q)
    
    def generate_k(self,y):
        return mod(pow(y,self.private_key),q)

Bob = Entity(6)
Alice = Entity(9)

yB = Bob.generate_y()
yA = Alice.generate_y()

kB = Bob.generate_k(yA)
kA = Alice.generate_k(yB)

print(kB==kA)

        