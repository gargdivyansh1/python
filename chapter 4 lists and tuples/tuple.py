# tuple is kind of list which is unmutable 
# which store multiple values 

num = [1,2,4,5,5]
print(type(num)) # list

num1 = (2,4,4,5)
print(type(num1)) # tuple 

num2 = () # creating an empty tuple 

num3 = (2,) # creating tuple with only one entry 
# remember comma (,) is important otherwise it will consider it as an class of int

num4 = (7)

print(type(num2))
print(type(num3))
print(type(num4)) 

num5 = (1,2,3,4,5) # tuple with multi entry 
