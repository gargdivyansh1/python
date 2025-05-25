# shift + alt + downarrow to replicate a line 

# to take input from the user 

# input take the input in the form of strings 

a = input("Enter a number 1 ")
b = input("Enter a number 2 ")

# here we are converting the input into integer directly 
# making string input in the integers 
c = int(input("Enter a number 3 ")) 
d = int(input("Enter a number 4 ")) 

print(a)
print(b)

# here we get the value like ab
# means if we have given a = 1 and b = 4 
# then the output is 14
# this is because input take the input in the form of strings 
# and string 1 + string 2 
# ram + shyam = ramshyam 
# "1" + "2" = 12
print(a+b) # output will be "a" + "b"

# printing the converted integers from strings values 
print(c+d) # output will be a + b 

# for knowing the type of the variable
print(type(a))
print(type(b))
print(type(c))
print(type(d))