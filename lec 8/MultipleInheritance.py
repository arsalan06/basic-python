class Car:
    @staticmethod
    def start():
        print("start car")
    @staticmethod
    def stop():
        print("stop car")

class Truck:
    @staticmethod
    def start():
        print("start Truck")
    @staticmethod
    def stop():
        print("stop Truck")

class ToyotaCar(Car, Truck):
    def __init__(self, name):
        self.name=name
car1=ToyotaCar("Fortuner")
car2=ToyotaCar("Prius")
print(car1.start())