name=[('Umang','Pratham','Divyaksh','Shivam'),'hitanshi','Divya','Uma']
bname=[]
gname=[]
bc=0
gc=0
print(name)
for x in name:
    if isinstance(x,tuple):
        bc +=len(x)
        bname= bname+list(x)
    else:
        gc+=1
        gname.append(x)
print("no. of boys =",bc)
print("no. of girls =",gc)
print("List of boys =",bname)
print("List of girls =",gname)      
      

      

