"""
Very important concept in the software industry
Method Overriding is the second type of polymorphism

Concept of Method overriding
when i dont have a phone so i told my fathers phone
after few months i got a  new phone
now i say i have redmi phone and not my phone
so my phone overrides my father's phone when someone asks which phone you have


"""

class A:
    def show(self):
        print(" IN A then show")



class B(A):   # WE use the concept of inheritance
    def show(self):
        print("IN MY show")   #here Class B overrides the class A


a1 = B()
a1.show()