class Computer():
    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print("Config is", self.cpu, self.ram)


com1 = Computer("i5", "8gb")
com2 = Computer("Rizen 8", "25gb")
com1.config()
com2.config()


