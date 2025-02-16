def sequare(num): return num*num
# lambda num : num * num


print(sequare(2))


def addTwo(num): return num+2
# lambda num : num + 2


print(addTwo(2))


def funcBuilder(x):
    return lambda num: num + x


add_ten = funcBuilder(10)
add_twenty = funcBuilder(20)

print(add_ten(7))
print(add_twenty(7))

########################


numbers = [3, 7, 12, 18, 20, 21]

squared_nums = map(lambda num: num * num, numbers)

print(list(squared_nums))

###############################

odd_nums = filter(lambda num: num % 2 != 0, numbers)

print(list(odd_nums))

#############################
