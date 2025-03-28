lst= ['madam','Python', "malayalam",12321]
def ispalindrome(s) :
    s = str(s)
    print(s,s[::1])
    return True if s==s[::-1] else False
for x in lst:
    print( x, ispalindrome(x))

    
   
    
         
