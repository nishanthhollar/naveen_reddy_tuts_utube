#basic factorial



# n = int(input("Enter the number to find out the factorial: "))
#
# def fact(n):
#     f = 1
#     for i in range(1, n+1):
#         f = i*f
#
#     return f
#
#
# result = fact(n)
# print(result)




#USing recursion
""" 
Recursion calling the function itself
The function calling again and again
Infinite calling in the IDE the limit is 1000 it's not so if you are doing some customization
"""



#Recursion
# import sys
# print(sys.getrecursionlimit())  #to get the limit of recursion
# sys.setrecursionlimit(10000)  #to set the recursion limit
# print(sys.getrecursionlimit())
# def greet():
#     print('Yo')
#     greet()



#FACTORIAL USING RECURSION
a = int(input('Enter the number to find the factorial: '))
def fact(n):
    if n == 0:
        return 1
    else:
        return n*fact(n-1)

result = fact(a)
print(result)



