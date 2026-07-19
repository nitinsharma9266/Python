'''def rem(l1,word):
    for item in l1:
        l1.remove(word)
        return l1


l1=['a','d','f','g','h']
print(rem(l1,'g'))

'''


def rem(l1,word):
    n=[]
    for item in l1:
        if not(item==word) :
            n.append(item.strip(word))
        
    return n


l1=["harry","nitin","rohan","an"]
print(rem(l1,"an"))