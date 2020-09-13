from numpy import*



#adding an element
arr = array([1, 2, 3, 4, 5])
res = arr + 5
print(sort(res))
print(res)

#adding two arrays
arr1 = array([1, 2, 3, 4, 5])
arr2 = array([6, 7, 8, 9, 10])
sum = arr1 + arr2
print(sum)
print(sort(sum))
print(min(sum))
print(max(sum))
print(concatenate([arr1 + arr2 ]))
print(sin(arr1))
print(log(arr1))
print(sqrt(sum))

print()
arr2 = arr1
print(arr1)
print(arr2)

print(id(arr1))
print(id(arr2))


arr2 = arr1.view() #has different addresss even if the value is same
arr1[1] = 0

print(arr1)
print(arr2)
print(id(arr1))
print(id(arr2))

arr1 = array([5, 6, 7, 8, 9])
arr2 = array([8, 9, 7, 4, 2])
arr2 = arr1.copy()  #very impt function which is used for deep copying
arr1[1] = 0
print(arr1)
print(arr2)
print(id(arr1))
print(id(arr2))
