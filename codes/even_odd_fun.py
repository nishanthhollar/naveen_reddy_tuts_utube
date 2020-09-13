

#PASS LIST TO FUNCTION IN AN ARGUMENTS
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 20]

def count(lst):
    e = 0
    o = 0
    for i in lst:
        if i%2 == 0:
            e += 1
        else:
            o += 1
    return e, o

even, odd = count(lst)
print(even)
print(odd)

print("Even : {} and Odd : {} ".format(even, odd))