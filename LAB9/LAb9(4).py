def sum_avg (marks):
        total=sum(marks)
        average= total/len(marks)
        return total,average
marks =[60,70,30,50]
print(sum_avg(marks))
