"""  Types of variables
There are two types
instance
class

"""



class Car():

    wheels = 10
    def __init__(self):
        self.mil = 10
        self.com = "BMW"

c1 = Car()
c2 = Car()

c1.mil = 8
c1.com = "BENZ"


print(c1.com, c1.mil, c1.wheels)
print(c2.com, c2.mil, c1.wheels)