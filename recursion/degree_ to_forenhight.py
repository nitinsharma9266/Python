def convert(n):
    faherenhight=(n*1.8)+32
    
    return faherenhight
    
n=int(input("enter degree in celsius :"))
ans=convert(n)
print(n,"degree celsius is equal to",ans ,"forenhight")