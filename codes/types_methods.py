


class Student():

    school = "Hollas"

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return(self.m1 + self.m2 + self.m3) / 3

    # def get_m1(self):
    #     return  self.m1
    #
    # def set_m1(self, value):
    #     self.m1 = value
    @classmethod
    def info(cls):
        return cls.school

    @staticmethod
    def infq():
        print("THis method has nothing to do with class variables or instance variables then we are using this mehod that is static method ")
        print("THis method is static")






s1 = Student(56, 78, 98)
s2 = Student(78, 67, 56)

print(s1.avg())
print(s2.avg())
print(Student.info())
Student.infq()