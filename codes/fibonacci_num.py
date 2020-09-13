#FIBONACCI NUMBER

x = 0
y = 1
temp = 0

z = int(input("Enter the number: "))

if z==1:
    print(x)
elif z<1:
    print("Invalid number!!")
elif z>1:
    print(x)
    print(y)
    for i in range(2, z):
        sum = x+y
        temp = sum
        x = y
        y = sum
        print(sum)



