count = 1


def greeting(name):
    # it will not work like this if you are trying to update global variable it will asume you are creating a new varible
    # count += 1
    # it will work like below
    global count
    count += 1
    print(count)
    color = "red"

    def welcome():
        # this is not work like below because python will assume color is a new variable
        # color = "blue"
        # change parent color value
        nonlocal color
        color = "green"
        print(color)

    welcome()


greeting("Arslan")
