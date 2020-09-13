

""" LINEAR SEARCH """

#program1
# list = [10, 20, 30, 40, 50, 60]
#
# def Search(a):
#     for i in len(list):
#         if (a == list[i]):
#             return("Element is present in the list")
#         else:
#             return("Element is not present in the list")
#
# a = int(input("Element to be searched: "))
# print(Search(a))




#program2 by naveen reddy
# pos = -1
# list = [10, 20, 30 , 40 , 50]
# n = int(input("Enter the element to be searched: "))
# def search(list, n):
#     i = 0
#     while i < len(list):
#         if list[i] == n:
#             globals() ['pos'] = i
#             return True
#         i+=1
#
#     return False
#
# if search(list, n):
#     print("FOUND at", pos)
# else:
#     print("NOT FOUND")





#porgram3 - linear search using for loop
pos = -1
list = [10, 20, 45, 56, 67, 45, 87]
n = int(input("Enter the number to be linear searched: "))
def search(list , n):
    for i in range(len(list)):
        if list[i] == n:
            globals() ['pos'] = i
            return True
    return False

if search(list, n):
    print("Found at", pos)
else:
    print("ELEMENT NOT FOUND")











