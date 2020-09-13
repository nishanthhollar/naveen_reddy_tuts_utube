def update(x):

    print(id(x))



    x = 8
    print(id(x))
    print("x", x)


lst = [10, 25, 30]
print(id(lst))
update(lst)
print("lst",lst)


#