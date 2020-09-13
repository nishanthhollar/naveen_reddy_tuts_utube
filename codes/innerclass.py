

class Student():

    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
        # self.lap = self.Laptop()

    def show(self):
        print(self.name, self.roll_no)

    class Laptop():

        def __init__(self):
            self.brand = "HP"
            self.cpu = "i5"
            self.ram = 8

        def show(self):
            print(self.brand, self.cpu, self.ram)




s1 = Student("Jenny", 67)
s2 = Student("Robert", 79)


# print(s1.lap.brand)
# lap1 = s1.lap           #to fetch the values of lap we need to specify s1.lap.brand
# lap2 = s1.lap           #initializing lap2 = s1.lap (lap is an object defined in the outer class)

s1.show()
s2.show()
# lap1.show()
# lap2.show()

#without creating object in outer class i am performing these kinds of functions
lap1 = Student.Laptop()
lap1.show()