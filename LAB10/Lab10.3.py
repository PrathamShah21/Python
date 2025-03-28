import random
ran = set()
while len(ran) <10:
    ran.add(random.randint(-15,15))
print(ran)
def square(n):
    return n*n

print(list(map(square,ran)))

                  
