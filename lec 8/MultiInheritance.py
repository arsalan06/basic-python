class Car:
    @staticmethod
    def start():
        print("start car")
    @staticmethod
    def stop():
        print("stop car")

class ToyotaCar(Car):
    def __init__(self, brand):
        self.name=brand

class Fottuner(ToyotaCar):
    def __init__(self, type):
        self.type=type
car1=ToyotaCar("diesel")
print(car1.start())