"""  THREE TYPES OF INHERITANCE
1> SINGLE LEVEL INHERITANCE
2>MULTI LEVEL INHERITANCE
3> MULTIPLE INHERITANCE
"""


class A():


    def __init__(self):
        print("in A init")


    def feature1(self):
        print("Feature 1 is working")

    def feature2(self):
        print("Feature 2 is working")



class B(A):   #sub class B inheriting features from A   class B(inherits parent class)
    def feature3(self):
        print("Feature 3 is working")

    def feature4(self):
        print("Feature 4 is working")
#
# class C(B):
#     def feature8(self):
#         print("Hey this is 8th feature that's working")
#
# a1 = A()
# a2 = A()
#
# b1 = B()
# c1 = C()
# c1.feature1() #accessing methods from class A
# c1.feature4() #accessing methods from class B
# a1.feature1()
# a2.feature2()
# b1.feature3()
# b1.feature1()

# a1 = A()

class D:
    def __init__(self):
        print("in  D init")

    def feature1(self):
        print("1111")


class E:
    def __init__(self):
        # super(E, self).__init__()
        super().__init__()
        print("In E init")

    def feauture4(self):
        print("4444")


# d1 = E()

class F(D, E):
    def __init__(self):
        super().__init__()
        print("in F init")

    def feat(self):
        super().feature1()

f = F()
f.feature1()
f.feauture4()
f.feat()