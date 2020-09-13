from array import *

# { from array import *  }- to import all the values
# import array as arr


# #for just integers
# vals = array('i',[1, 5, 6, 90, 56] ) #here we specify the type
# print(vals)

# vals = array("i", [1, 6, 7, 8, 0])
# vals.reverse()
# print(vals[2])
# print(vals.buffer_info())
# print(vals.typecode)


#
# vals = array("i", [1, 6, 7, -8, 0])
# vals.reverse()
# for i in range(len(vals)):
#     print(vals[i])


#
# vals = array("i", [1, 6, 7, -8, 0])
# vals.reverse()
# for e in vals:
#     print(e)


#
# vals = array('u', ['a', 'e', 'i', 'o', 'u'])
# # print(vals.buffer_info())
# # print(vals.typecode)
# for ch in range(len(vals)):
#     print(vals[ch])


# vals = array('u', ['a', 'e', 'i', 'o', 'u'])
# for ch in vals:
#     print(ch)

# #for loop
# vals = array('i', [1, 4, 5, 7, 10])
# newArr = array(vals.typecode, (a*a for a in vals))  #i am taking values from other arrays and squaring it
#
#
# for e in newArr:
#     print(e)




# #USing while loop
# vals = array('i', [1, 4, 5, 7, 10])
# newArr = array(vals.typecode, (a*a for a in vals))
# i = 0
# while i<len(newArr):
#     print(newArr[i])
#     i +=1