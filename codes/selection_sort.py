"""
SELECTION SORT
"""
def sort(nums):

    for i in range(6):
        minpos = i
        for j in range(i, 6):
            if nums[j] < nums[minpos]:
                minpos = j

        temp = nums[i]
        nums[i] = nums[minpos]
        nums[minpos]  = temp


        print(nums)





nums = [5, 3, 4, 2, 1, 10]
sort(nums)
print(nums)