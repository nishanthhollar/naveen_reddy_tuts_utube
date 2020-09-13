from numpy import *
arr = array([2, 5, 8, 23, 56])
print(arr)
max = arr[0]
for i in range(len(arr)):
    if arr[i]>max:
        max = arr[i]
print(max)