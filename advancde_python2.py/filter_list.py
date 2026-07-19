l = [2,4,5,6,10,16,15,50]

def divisible(n):
    return n % 5 == 0   # 5 se divisible ho to True

onlydivisible = filter(divisible, l)
print(list(onlydivisible))   # output: [5, 10, 15, 50]
