f = lambda a : a*a #anonymous function which  we need not define


result = f(5)
print(result)



d = lambda a,b : a*b #anonymous function passing two arguments
result = d(4, 5)
print(result)



#FILTER MAP AND REDUCE

#FIlter

def is_even(n):
        return n % 2 == 0



nums = [1, 2, 3, 5, 6, 8, 20, 34, 54, 77]
evens = list(filter(is_even, nums))
# result = filter(function, iterable)
# ans = list(filter(is_even(nums), nums))
print(evens)

#my code
f = lambda a: a%2 == 1

numbers = [10, 33, 45, 667, 798, 788, 565]
odds = list (filter(f , numbers))
print(odds)

#proper code
numbr = [10, 20 , 33, 23, 24, 44, 56]
evens = list(filter(lambda a : a%2 == 0, numbr))
print(evens)


#MAP is used to atler or change the values
doubles = list(map(lambda n: n*2, evens))
add2 = list(map(lambda n: n+2, evens))
print(doubles)
print(add2)


#REDUCE
from functools import*



#using normal function
def add_all(a, b):
    return a+b

sum = reduce(add_all, doubles)
print(sum)

#using lambda
add = reduce(lambda a,b : a+b, doubles)
print(add)



