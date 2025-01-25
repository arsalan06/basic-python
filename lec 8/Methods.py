class Student:
    # default counstructor
    # def __init__(self):
    #     pass
    @staticmethod  # decorator
    def college():
        print("hello i am a static method")
    # # parameterize constructor

    def __init__(self, fullName, marks):
        self.name = fullName
        self.marks = marks
        print("add new student")
    # Method

    def Welcome(self, name):
        print("welcome in first Method", self.name)


s1 = Student("Arslan", 88)
s1.Welcome("hdhf")
s1.college()
# second way to call amd pass params
# s1=Student()
# s1.Welcome("Arslan")
