n=int(input("enter the number : "))

str_num=str(n)

reverse_num=str_num[: :-1]

reverse=int(reverse_num)

if(n==reverse):
    print("the number is palindrom ")

else:
    print("the number is not palindrom ")