"""
BINARY SEARCH ALL THE VALUES SHOULD BE SORTED
"""


#program1
pos = -1

list = [50, 20, 45, 56, 67, 45, 87, 1003993, 8454546]
sort = sorted(list)
n = int(input("Enter the number to be binary searched: "))
def search(sort , n):
    lb = 0
    ub = len(sort) - 1

    while lb <= ub:
        mid = (lb+ub) // 2

        if list[mid] == n:
            globals()['pos'] = mid
            return True
        else:
            if sort[mid] < n:
                lb = mid+1
            else:
                ub = mid-1
    return False


if search(sort, n):
    print("Found at", pos)
else:
    print("ELEMENT NOT FOUND")



#program 2