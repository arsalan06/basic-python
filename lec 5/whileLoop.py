count=1
while count<=5:
    print("hello world")
    count +=1

print(count)

nums=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
i=0
while i<len(nums):
    print("here is:", nums[i])
    i =i+1

# find a number in tuple
x=77
rray=(1,2,3,20,22,34,40,44,50,55,60,66,70,77,80,88,90,98,100)
j=0
while j<len(rray):
    if(rray[j]==x):
        print("your number found :", rray[j])
        break
    else:
        print("your number not found :", rray[j])
    j +=1