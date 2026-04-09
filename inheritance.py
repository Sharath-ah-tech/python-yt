class Man:
    def __init__(self, name):
        self.name = name


class Work(Man):   
    def working(self):
        print(f"{self.name} is working")

    def not_working(self):
        print(f"{self.name} is not working")


class Sleep(Man):  
    def sleeping(self):
        print(f"{self.name} is sleeping")

    def not_sleeping(self):
        print(f"{self.name} is not sleeping")
w = Work("John")
s = Sleep("John")
w.working()
s.sleeping()