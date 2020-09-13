
"""  COmparing of the objects using certain methods """

class Computer():
    def __init__(self):
        self.name = "Nishanth"
        self.age = 21

    def update(self):
        self.age = 30

    def compare(self, other):
        if self.age == other.age:
            return True
        else:
            return False


com1 = Computer()
com2 = Computer()


# print(id(com1))  #everytime we run this program we get different address as it creates new space in the heap memory
# print(id(com2))  #memory allocation is done by constructor

com1.name = "Varuni"  #changing name of com1
com1.age = 30
print(com1.name, com1.age)
print(com2.name, com2.age)



print(com1)    #if i do this then we can only get the addresss
print(com1.age)
print(com2.age)


#comparing of age
if com1 == com2:  # this codes compares the addresss
    print("THey are same")
com1.update()
if com1.compare(com2):
    print("they are same")
else:
    print("FUCK OFF")
