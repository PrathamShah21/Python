def concdict() :
    d1={0:'zero',1:'one', 2:'two'}
    d2={3:'three',4:'four', 5:'five'}
    d3={6:'six', 7:'seven', 8:'eight',9:'nine'}
    d4={**d1,**d2,**d3}
    print(d4)
concdict()

