def compute(no):
        s = 0
        for i in range(1,5):
            s += int(no*1)
        return s
def compute2(no):
        s = 0
        n = no
        for i in range(1,5):
            s += (10*no+n)
        return s    
for x in range(4,8):
        print(compute(x))
for x in range(4,8):
        print(compute2(x))        
