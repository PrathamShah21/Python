import  random
X={ random.randint(15,45) for i in range(10) }
S1=set()
c=0
for i in X:
    if i<30:
        c=c+1
for i in X:
    if i<36:
        S1.add(i)
             
print(X,c,S1)
