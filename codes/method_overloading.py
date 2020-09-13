
#METHOD OVERLOADING NOT PRESENT IN PYTHON

class Student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def sum(self, a = None, b = None, c = None): #here it takes only two arguments


        if a != None and b!= None and c!= None:
                s = a+b+c

        elif a!=None and b != None:
                s = a+b

        else:
                s = a
        return s



s1 = Student(50, 40)

#print(s1.sum(5, 9))  # here we are passing only two arguments


#if we pass three arguments
print(s1.sum(5))