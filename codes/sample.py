# from array import *
# arr = array('i', [])
# n = int(input("Enter the size of the array: "))
#
# for i in range(n):
#             x = int(input('Enter the elements to be entered into the array: '))
#             arr.append(x)
#
# largest = max(arr)
#
#
# for i in range(n):
#     if largest == max(arr):
#         arr.remove(max(arr))
#
# print(max(arr))

n = int(input())
arr = map(int, input().split())
largest = max(arr)
print(largest)
d = arr
print(d)
# for i in range(n):
#     if largest == max(arr):
#         arr.remove(max(arr))
# print(max(arr))