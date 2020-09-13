




# #to insert an user element in an array we use the method append
#
# from array import *
# arr = array('i', []) #empty array
#
# n = int(input("Enter the length of the array: "))
#
# for element in range(n):
#     x = int(input('Enter the values to be entered into the array: '))
#     arr.append(x)
#
#
# print(arr)
#
# """ Manually checking or searching the numbers """
# val = int(input('enter the element which you want to search baby: '))
# k = 1
# for e in arr:
#     if e==val:
#         print("THe element exists",e)
#         break
#         k+=1
#
# else:
#     print("element does not exist")



from array import *

arr = array('u', [])
n = int(input("Enter the length of the array: ")) #determine the length of the array

for element in range(n):
    x = input("Enter the vowels you wish to enter: ")
    arr.append(x)

print(arr)

#now to search for the vowels
vals = input("Enter the vowel to be searched: ")
# for e in arr:
#     if vals==e:
#         print('Element found',e)
#         break
# else:
#     print("Element not found")

print(arr.index(vals))   #it is the automatic method
# #ALL THIS IS DONE MANUALLY
# #now to search for the index of the vowel
# vals = input("Enter the vowel to be searched to get index: ")
# k = 0
# for e in arr:
#     if vals==e:
#         print('Element found',e)
#         print(k)
#         break
#
#     k +=1
# else:
#     print("Element not found")



