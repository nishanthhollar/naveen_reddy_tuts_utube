
def topten():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5






# values = topten()
# print(values.__next__())
# print(values.__next__())



def Myten():
    n =  1

    while n <= 10:
        sq = n * n
        yield sq
        n += 1

values1 = Myten()

for i in values1:
    print(i)