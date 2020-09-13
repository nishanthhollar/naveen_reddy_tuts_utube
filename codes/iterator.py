nums = [7, 8, 9, 5]

print(nums[3])

# for i in nums:
#     print(i, end="\t")

it = iter(nums)


print(it.__next__())
print(it.__next__()) #another way of using iterator

print(next(it)) #another way of using iterator



for i in nums:
    print(i)




class Topten:
    def __init__(self):  #counter variable
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):

        if self.num <= 10:
            val = self.num
            self.num += 1


            return val
        else:
            raise StopIteration


values = Topten()

print(next(values))  # if we have used next here  then it is not going to repeat


for i in values:
    print(i)











