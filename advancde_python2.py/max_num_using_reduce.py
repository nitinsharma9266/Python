from functools import reduce

l=[56,67,12,34,14,78,54,45]

def greater(a,b):
    if(a>b):
        return a
    return b
print(reduce(greater,l))

