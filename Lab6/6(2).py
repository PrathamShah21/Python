def tuple2():
    l= [(102,'Umang',18),(106,'Divyaksh',18),(110,'Pratham',18)]
    print(l)

    rn=[]
    nm=[]
    age=[]
    for x in l:
        rn.append(x[0])
        nm.append(x[1])
        age.append(x[2])
    print(rn,nm,age)
tuple2()
