from datetime import date
d1 = (3,10,2005)
d2 = (1,8,2006)
date1 = date(d1[2],d1[1],d1[0])
date2 = date(d2[2],d2[1],d2[0])
datediff = abs(date2-date1)
print('Difference between date',date1,'&',date2,'is',datediff)

