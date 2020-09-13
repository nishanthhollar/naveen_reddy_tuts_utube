""" Swap two Numbers in python """

# #program1 Method1
# '''Using temp variable or third variable '''
# a = 10
# b = 16
# temp = 0
#
#
#
# temp = a
# a = b
# b = temp
#
#
# print(a)
# print(b)


#this has a problem because we are wasting a variable






#program2 - Method 2 Using formula

""" THE FORMULA IS 
      a = a + b
      b = a - b
      a = a - b
      """
#
# a = 10
# b = 20
#
# a = a + b   # here a+b = 30
# b = a - b   # b = 30 - 20 = 10 which is the value of a
# a = a - b   # a = 30 - 10 = 20 which is the value of b
#
# print(a)
# print(b)


#THis has a problem as we are wasting bits

# a = 2 which has 2 bits 10
# b = 3 which has 2 bits 11
# a+b = 5 which has 4 bits  0101
# hence two bits extra there program not efficient





#program3 - this way is done by using XOR Method


# a = 5
# b = 6
#
# a = a ^ b #using XOR
# b = a ^ b
# a = a ^ b
#
# print(a)
# print(b)




#program 4 - The best Method uSed in Python very unique method

a = 20
b = 30

a, b = b, a #Using the concept of Stack Rotation which rotates the topmost two stack variables of python
""" Here python evaluates the right hand expression first and then it evaluates the left hand expression 
USes rot_two() function - which rotates the topmost two values of the stack
"""

print(a)
print(b)