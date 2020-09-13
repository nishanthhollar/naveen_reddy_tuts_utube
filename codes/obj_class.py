class Computer():

    def config(self):
        print("i5, 16gb, 3TB")

com1 = Computer()  #constructor  obj = class_name()
com2 = Computer()

print(type(com1))


Computer.config(com1)  #way of calling objects
Computer.config(com2)   #way of calling objects

com1.config()   #way of calling objects
com2.config()   #way of calling objects
