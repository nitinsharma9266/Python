import numpy as np
a=np.array([[1,2,5,3]])
"""print("add 1 to every elements :",a+1)
print("subtract 3 from each elements :",a-3)
print("Multiply each elements by 10 :",a*10)
print("Square of each elements :",a**2)
#modify array
a*=2
print("Double each elements of original array :",a)
a=np.array([[1,2,3],[3,4,5],[6,7,8]])
print("\nOriginal array\n",a)
print("Transpose of array :",a.T)"""

"""import numpy as np

# 1. Array Creation
a = np.array([1, 2, 3, 4, 5])
b = np.array([10, 20, 30, 40, 50])

print("Array a:", a)
print("Array b:", b)

# 2. Arithmetic Operations
print("\nAddition:", a + b)
print("Subtraction:", b - a)
print("Multiplication:", a * b)
print("Division:", b / a)
print("Power:", a ** 2)

# 3. Indexing and Slicing
print("\nFirst element:", a[0])
print("Last element:", a[-1])
print("Slicing (1 to 3):", a[1:4])

# 4. Reshape
c = np.array([1, 2, 3, 4, 5, 6])
reshape_arr = c.reshape(2, 3)
print("\nReshaped Array:\n", reshape_arr)

# 5. Flatten
print("\nFlatten:", reshape_arr.flatten())

# 6. Transpose
print("\nTranspose:\n", reshape_arr.T)

# 7. Statistical Operations
print("\nSum:", np.sum(a))
print("Mean:", np.mean(a))
print("Max:", np.max(a))
print("Min:", np.min(a))
print("Standard Deviation:", np.std(a))

# 8. Searching Operations
print("\nIndex where value > 3:", np.where(a > 3))
print("Index of max value:", np.argmax(a))
print("Index of min value:", np.argmin(a))

# 9. Sorting
unsorted_arr = np.array([5, 2, 8, 1, 9])
print("\nSorted Array:", np.sort(unsorted_arr))

# 10. Joining Arrays
joined = np.concatenate((a, b))
print("\nConcatenated Array:", joined)

# 11. Splitting Arrays
split_arr = np.split(joined, 2)
print("\nSplit Arrays:", split_arr)

# 12. Mathematical Functions
print("\nSquare Root:", np.sqrt(a))
print("Sine:", np.sin(a))
print("Log:", np.log(a))

# 13. Boolean Filtering
print("\nElements greater than 3:", a[a > 3])

# 14. Matrix Operations
x = np.array([[1, 2], [3, 4]])
y = np.array([[5, 6], [7, 8]])

print("\nMatrix Multiplication:\n", np.dot(x, y))
print("Determinant:", np.linalg.det(x))
print("Inverse:\n", np.linalg.inv(x))"""
# 3x3 matrix with values ranging from 2 to 10.

"""matrix=np.arange(2,11).reshape(3,3)
print("3x3 dimention matrix :",matrix)"""

# write a program to reverse an array 
"""original_array=np.array([1,2,3,4,5,6])
reverse_array=original_array[::-1]
print("original array ", original_array)
print("reverse array ",reverse_array)"""

def find_longest_word(file_name):
    longest_word=" "
    with open(file_name,'r') as file:
        for line in file:
            words=line.split()
            for word in words:
                if len(word)>len(longest_word):
                    longest_word=word
        return longest_word
file_name="example.txt"
longest_word=find_longest_word(file_name)
print("the longest word in the file\n",longest_word)
