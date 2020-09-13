

#the main function which the user doesn't have access to
def div(a, b):
    print(a/b)


#the modification function the programmer codes
def smart_div(func):

    def inner(a, b):
        if a<b:
            a, b = b, a
        return func(a, b)

    return inner

div1 = smart_div(div)

div1(2, 4)



#MY copied function
def sub(a,b):
    print(a-b)


def smart_sub(func):#we are calling div indirectly

    def inner(a, b):
        if a<b:
            a, b = b, a
        return func(a, b)
    return inner

#newnamevariable = programmerdefinedfunc(existing function)
sub = smart_sub(sub)
sub(1, 4)


#python is a beauty as we take functions as a parameter
