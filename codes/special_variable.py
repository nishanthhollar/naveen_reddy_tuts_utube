

# import spclvar2
# print("DEMO SAYS: "+ __name__)



#
# def main():
#     print("Hello")
#     print("Welcome User")
#
# if __name__ == "__main__":
#     main()

import spclvar2
from spclvar2 import add
def fun1():
    add()
    print("from fun1")

def fun2():
    print("from fun2")

def main():
    fun1()
    fun2()
if __name__ == "__main__":   #important code
    main()
