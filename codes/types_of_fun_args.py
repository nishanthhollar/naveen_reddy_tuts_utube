


""" There are two types of arguments
1) FORMAL ARGUMENTS
2) ACTUAL ARGUMENTS

Formal arguments are defined at the beginning
Actual arguments are passed when the function is being called
Actual Arguments are of  4 types
1. Position
2. Keyword
3. Default
4. Variable Length
"""

def add(a, b):  #Formal Arguments
    c = a + b
    print(c)

add(10, 35)        #Actual Arguments



#Position arguments


def person(name, age):
    print("My name is:", name)
    print("My age is:", age)

person("Nishanth", 22)

""" 
 How will we knoe nishanth is going to name and 22 is going to age 
THis is following position arguments
What if i don't know the sequence
"""

def person1(name, age):
    print("My name is", name)
    print('My age is', age)

person(28, "naveen")      #this will work but look at the operation as it is not giving
                        #the desired output


#KEYWORD ARGUMENTS
""" HEre we are using Keywords while calling the function example"""

def person2(age, name): #here the order does not matter as we are not using position
    print('My Name is', name)
    print("My age is", age)

person2 ( name = "Nishanth", age= 22) #here we are using keywords but we are reversing the order




#DEFAULT ARGUMENTS IN FUNCTIONS

def person5(name, age = 18):  #this is the default value that i am mentioning over here only
    print("The person's name is:", name)
    print("The person's age is:", age)

person5('nishanth')    #just sending only one argument



#VARIABLE LENGTH ARGUMENTS

def sum(a, *b):   #* ---> star means that b is referring to multiple values in a tuple
    print(a)
    print(b)
    c = a
    for i in b:
        c = c + i

    print(c)

sum(5, 6, 11, 45)
