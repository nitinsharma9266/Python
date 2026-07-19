from functools import reduce
# Map example
l=[1,4,6,3,7,8]
square=lambda x:x*x
sqlist=map(square,l)
print(list(sqlist))


# Filter example

def even(n):
    if(n%2==0):
        return True
    return False
onlyeven=filter(even,l)

print(list(onlyeven))

#Reduce example
def sum(a,b):
    return a+b
print(reduce(sum,l))