def dict4():
    str = input("Enter a string:")
    d = {}
    for ch in str:
        if ch not in d.keys():
            d[ch]= str.count(ch)
    print(d)
dict4()
