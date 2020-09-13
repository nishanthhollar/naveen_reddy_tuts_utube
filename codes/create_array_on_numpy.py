"""
6 types of array creation on numpy
1. array()
2. linspace() - linespace(start, stop, part)  by default it creates 50
3. logspace()  - logspace(start, stop, gap) - in linespace gap btw 2 elements is fixed but in logspace it is not fixed
4. arange()    - arrange(first, last, step)
5. zeros()- by defualt makes all values 0
6. ones() - by default makes all values 1


"""



from numpy import *


#1...array() function without specifying the type
arr = array([1, 3, 5, 6, 8])
print(arr)

#1..... array() function with specifying the type

arr = array(['A', "E", "I", 'O', "U"], str)
print(arr)
print(arr.dtype)


#2.....linspace()
arr = linspace(1, 20, 10)
print(arr)

#2...linspace() by default it divides into 50 parts
arr = linspace(1, 16)
print("%.2f"%arr[6])

#3 logspace() divides by log where the space is not the same as linspace
arr = logspace(1, 10, 10)
print(arr)

#4...arange()
arr = arange(1, 10, 2)
print(arr)

#4 arange() default is 1 and here 10 is not included
arr = arange(1, 10)
print(arr)

#5 zeros() default will be float values
arr = zeros(10)
print(arr)

#ones() default will be float values
arr = ones(10)
print(arr)