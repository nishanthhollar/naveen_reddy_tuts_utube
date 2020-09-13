"""
Take names from the user and count if the user names have more than 5 letters or not

"""



# lst = []
#
# n = int(input("Enter the number of list items:"))
# for i in range(n):
#     x = input("Enter the names you need to enter in the list ")
#     lst.append(x)
#
# print(lst)
#
# def calci(lst):
#     for item in lst:
#         if len(item)>= 5:
#             print("The count is greater than 5: ", item, item.count())
#
#         else:
#             print("THe count is less than 5", item)
#
# calci(lst)



#program2
names = []
n = int(input("enter the number of names:"))

def insert():
    for i in names:
        x = int(input("NExt Name to store: "))
        names.append(x)

print(names)

def calculate(names):
    for i in names:
        count = 0
        if len(i)>5:
            print("Name: {}, Length: {}".format(i, len(i)))
            count +=1

        print("The count is", count)
calculate(names)