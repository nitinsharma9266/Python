"""
*
* *
*  *
*   *
*********
"""
"""rows=5

for i in range(rows):
    if i==0:
        print("*")
    elif i == rows - 1:
        print((2 * rows - 1) * "*")
    else:
        print("*"+i*" "+"*")
    """
"""import re
email = input("Enter email: ")
pattern = r'^[^@\s]+@[^@\s]+\.[^@\s]+$'
if re.match(pattern, email):
    print("Valid Email ✅")
else:
    print("Invalid Email ❌")"""
    

"""try:
    n=int(input("enter the number :"))
    result=10/n
except ZeroDivisionError:
    print("can't be solved ?")
except ValueError:
    print("entered wrong value ")
else:
    print("result is:",result)
finally:
    print("This always run clean work.")
    """
"""floor division example   
try:
    n=int(input("enter the value "))
    result=n//2
except ValueError:
    print("Invailid Input !")
else:
    print("Your result is :" ,result)"""
    
"""def char_freq(s):
    freq = {}   # empty dictionary

    for ch in s:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1

    return freq

result=char_freq("HELLO")
print(result)"""

"""import matplotlib.pyplot as plt

# Data
languages = ['Python', 'Java', 'C++', 'JavaScript', 'Ruby']
values = [30, 25, 20, 15, 10]

# Create Pie Chart
plt.pie(values, labels=languages, autopct='%1.1f%%')

# Title
plt.title("Programming Language Usage")

# Show chart
plt.show()"""

