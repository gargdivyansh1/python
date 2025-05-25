# to print name followed by any other string 

name = input("Enter your name: ")
another_name = "Hero."

# this f is used for printing the variables together without using any plus sign or the double quotes
print(name + "Hero.") # this will not include any space in between 
print(f"{name}{another_name}") # this will not include any space in between
print(f"{name} {another_name}") # this will include a space in between as provided
print(f"Good Afternoon, {name}") # this will also include the space 

print(f"{name} hello how are you? {another_name}") 
# by this we could understand that we can print the value of variables with the raw string too .. without using multiples + sign like "divyansh" + " " + another_name