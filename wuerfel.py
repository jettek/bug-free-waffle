from random import randint

n = 10
a = []

for i in range (1,n+1):

    b = randint(1,6)
    a.append(b)
c = sum(a)/n
print(c)
