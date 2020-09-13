



from numpy import *
arr1 = array([1, 2, 3, 4, 5])
arr2 = array([6, 7, 8, 9, 10])
for a, b in zip(arr1, arr2):
    print(a+b)


arr3 = empty(5)
for i in range(len(arr1)):
    arr3[i] = arr1[i] + arr2[i]
print(arr3)
