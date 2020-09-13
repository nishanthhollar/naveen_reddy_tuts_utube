"""

BUBBLE SORT
"""

def sort(list):
    for i in range(len(list)-1, 0, -1):
        for j in range(i):
            if list[j] > list[j+1]:
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp





# list = [2, 3, 1, 4]
list = [1, 2, 33, 56, 3, 5, 9, 7, 6, 4, 3]

sort(list)
print(list)