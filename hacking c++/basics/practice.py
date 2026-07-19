# size=5
# for i in range(size):
#     print("*"*size)

# for i in range(size):
#     print("*"*(i+1))

# for i in range(size):
#     count=size-i
#     print("*"*count)
    

# n = 5  # diamond ki height

# for i in range(1, n):
#     # Agar i <= n hai to stars badhenge, warna ghatenge
#     # if i <= n:
#     #     stars = i
#     # else:
#     #     stars = 2*n - i

#     # spaces ka hisaab (center ke liye)
#     spaces = n - i

#     print(" " * spaces + "*" * (2*i - 1))
    
# n = 5  # diamond ki height

# for i in range(1, 2*n):
#     # Agar i <= n hai to stars badhenge, warna ghatenge
#     if i <= n:
#         stars = i
#     else:
#         stars = 2*n - i

#     # spaces ka hisaab (center ke liye)
#     spaces = n - stars

#     print(" " * spaces + "*" * (2*stars - 1))

# n=int(input("enter the number : "))
# temp=n
# rev=0
# while(n>0):
#     rem=n%10
#     rev=rev*10+rem
    
#     n=n//10
    
# if(temp==rev):
#     print("the number is palindrom ")

# else:
#     print("the number is not palindrom.")

for i in range(5):
    for j in range(5):
        if(j==1):
            print(" ")
        else:
            print("*")
            
print()