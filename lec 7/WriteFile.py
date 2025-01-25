# w will overwrite the file
# f=open("D:\Python\lec 7\demo.txt", "w")
# f.write("i am going to append file")
# a will append the data in file
f=open("D:\Python\lec 7\demo.txt", "a")
f.write("i am going to append file")
# add new line
f.write("\ni am going to new line file")
f.close