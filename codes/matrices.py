from numpy import*
arr = array([
            [2, 3, 4, 7, 8, 9], [4, 5, 6, 7, 34, 56]
])
# print(arr)
# #converting two d array to one d array
# arr2 = arr.flatten()
# print(arr2)
#
# print(arr.dtype)  #type of the two d array
# print(arr.size)  #size of the array ie 6
#
# arr3 = arr2.reshape(3, 4)
# arr3 = arr2.reshape(2, 2, 2)
# print(arr3)
arr2 = arr.flatten()
print(arr2)

arr3 = arr2.reshape(2, 2, 3)
print(arr3)

m = matrix(arr)
print(m)
m = matrix('1 2 3; 4 5 6; 7 8 9')
print(m)
print(diagonal(m)) #to get diagonal elements
print(m.min())  #to get minimum
print(m.max()) #to get maximum

m = matrix('1 2 4; 5 6 7; 8 9 20')
m2 = matrix('3 4 5; 5 6 7; 5 3 2')
m3 = m + m2

print(m3)
m4 = m * m2;  #proper multiplication
print(m4)

m5 = m * m2  #doesn't matter if i put semi colon at the end or not for this operation
print(m5)