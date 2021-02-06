class Bird:
    def __init__(self):
        print("Bird is ready")

    def swim(self):
        print("Swim faster")

class Penguin(Bird):
    def __init__(self):
        print("Penguin is ready")
        super().__init__()
        print("Penguin is ready")

    def who(self):
        print("Penguin")

# obj = Bird()
# obj.swim()


obj2 = Penguin()
obj2.swim()
obj2.swim()