def dim1(x,v) :
        l=[]
        for i in range(x):
               l.append(v)
        print(l)
def dim2(x,y,v) :
        l=[]
        for i in range(x):
               m = []
               for j in range(y):
                     m.append(v)
                     

               l.append(m)
        print(l)        


dim1(5,3)
dim2(5,5,3)
