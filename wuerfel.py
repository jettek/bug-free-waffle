from random import randint
a = []
n = 10
for i in range (1,n+1):

    b = randint(1,6)
    a.append(b)
c = sum(a)/n
print(c)  
