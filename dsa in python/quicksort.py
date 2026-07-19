def quick_sort(list1):
    if len(list1)<=1:
        return list1
    else:
        pivot=list1[0]
        lasser=[x for x in list1[1:] if x<=pivot]
        greater=[x for x in list1[1:] if x>pivot]
        return quick_sort(lasser)+[pivot]+quick_sort(greater)
    
l1=[25,37,11,14,60,82,18,41]
result=quick_sort(l1)
print(result)