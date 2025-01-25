class Car:
    def __init__(self, type):
        self.type=type
    @staticmethod
    def start():
        print("start car")
    @staticmethod
    def stop():
        print("stop car")

class ToyotaCar(Car):
    def __init__(self, name, type):
        super().__init__(type)
        self.name=name
        super().start()
car2=ToyotaCar("Prius", "electric")
#if want to get the attribute of parent class like below it will not work we need to use Supper Method 
print(car2.type)    