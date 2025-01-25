class Car:
    @staticmethod
    def start():
        print("start car")
    @staticmethod
    def stop():
        print("stop car")

class ToyotaCar(Car):
    def __init__(self, name):
        self.name=name
car1=ToyotaCar("Fortuner")
car2=ToyotaCar("Prius")
print(car1.start())