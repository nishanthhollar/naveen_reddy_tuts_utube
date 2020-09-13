
class Pycharm:

    def execute(self):
        print("Spell Checking")
        print("Compiling")
        print("Running")

class Mycharm:

    def execute(self):
        print("I am execcuting and this is DUCK TYPING")




class Laptop:

    def code(self, ide):
        ide.execute()


ide1 = Pycharm()
ide2 = Mycharm()
lap1 = Laptop()
lap1.code(ide1)
lap1.code(ide2)
