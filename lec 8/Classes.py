class Student:
    #default counstructor
    def __init__(self):
        pass
    # parameterize constructor
    def __init__(self, fullName, marks):
        self.name=fullName
        self.marks=marks
        print("add new student")
    # name="arslan"
s1=Student("arslan", 88 )
print(s1.name)

# class Car:
#     color="blue"
# car1=Car()
# print(car1)