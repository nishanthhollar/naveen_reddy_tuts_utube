

n = int(input("Find the fibonacci sequence for the  number: "))
a = 0
b = 1
temp = 0
if n<1:
    print("Invalid input")
elif n==1:
    print(a)

elif n>1:
    print(a)
    print(b)

    for i in range(2, n+1):
        c = a+b
        a = b
        b = c

        print(c)






