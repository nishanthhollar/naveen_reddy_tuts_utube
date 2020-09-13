




# def person(name, *data):  #here data is a tuple
#         print(name)
#         print(data)
#
# person("nishanth", age = 18, city = 'Bangalore', mob = 813989984)



#Keyword Variable
def person(name, **data):
        print(name)

        for i,j in data.items():
            print(i, j)

person("nishanth", age = 20, city = "Bangalore", mob = 8888888)







#Understanding variable scope

a = 10

def something():
    a = 20
    print("in fun", a)


something()
print("out fun", a)

#When i change values of in function the out function values even though having the same value does not change



#therefore we use global variables

a = 20

def something1():
    global a
    a = 25  #here changing a value both in and out function changes
    print("IN fun which is a: ", a)
something1()
print("Out function in a", a)





#having a global and a local variable
a = 15
print(id(a))  #both of them pointing to the same memory location

def something1():

    a = 25
    x = globals()['a'] #both of the variables pointing to the same memory location
    print(id(x))
    print("IN fun which is a: ", a)
something1()
print("Out function in a", a)
