"""CHECK FOR PRIME NUMBERSS
prime number is a number which is i=divisible by only 1 or itself
step1> try to check if the number can be divided by 2
if yes then it is a prime number else it is not a prime number
Step2> try to check for the numbers after 2 till num//2 and see if it is divisible"""







# num = int(input('Check the number for if it is prime or not prime: '))
#
# if num>1:
#     for i in range(2, num//2):
#         if(num%i == 0):
#             print("Print it is not prime", i)
#             break
#         else:
#             print('The number is prime',i)
#
# else:
#     print("THe number is neither prime nor composite")


num = 23
for i in range(2, num//2):
    if num%i == 0:
        print("NOt prime")
        break
else:
    print("Prime")