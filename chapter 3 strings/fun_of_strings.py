name = "divyansh"

# to get the length of the string 
print(len(name))

# to check ending 
print(name.endswith("sh"))

# to check starting
print(name.startswith("d"))

# to make the starting letter of starting word capatalize
# This will only capitalize the first letter of the string 
print(name.capitalize())

# using the find method to check if a string is present in another string
num = "hey udhkjfhudsdhfh hhh ih shivam"

num1 = input("Enter your name : ")

if(num.find(num1)):
    print("YES")
else:
    print("NO")

# escape sequence characters 
# \n for the next line 
# \t for 4spaces # this could also be customised according to the need

# for using the actual backslash in the output we got 2 ways
# 1. \" .... \" for actual backslashes in output 
# 2. \\ for actul backslash