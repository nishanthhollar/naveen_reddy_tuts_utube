







# i = 1
# while i<=4:
#     print("#", end="")
#
#     j = 1
#     while j<=4:
#         print("#", end="")
#         j = j+1
#     i = i + 1
#     print()

#ASCENDING PATTERN
# for i in range(4): # i represents row
#     for j in range(4): #j represents column
#         print("#", end="")
#     print()


# #DESCENDING PATTERN
# for i in range(4): # i represents row
#     for j in range(4 -i): #j represents column
#         print("#",i, end="")
#     print()


# for i in range(5):
#     for j in range(5-i):
#         print(i,end="")
#         print()
#         print(j)


# for i in range(1, 5):
#     print(i, end="\t")
# print()
# for i in range(2, 5):
#     print(i, end="\t")
# print()
# for i in range(3, 5):
#     print(i, end="\t")
# print()
# for i in range(4, 5):
#     print(i, end="")


# for i in range(1,6):
#     for j in range(1, 6-i):
#         print(j, end="\t")
#     print()


for i in range(1,6):
    for j in range(1, 6-i):
        print(j, end="\t")
    print()