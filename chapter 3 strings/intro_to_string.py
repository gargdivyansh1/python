# strings are immutable means we cannot change the string

# if the indexing start from the left side then it start with 0 
# Harry = H = 0, a = 1, r = 2, r = 3, y = 4

# when the indexing start from the right side then it start with -1
# Harry = H = -5, a = -4, r = -3, r = -2, y = -1

# creating of strings 
name = "Divyansh"
print(name) # Divyansh

# to find length of string 
length = len(name)
print(length) # 8

# to get the substring of any string 
# starting index is included but the ending index is not included 

# when we miss to write the starting index then it will take value of index 0 and will print from the start till the end index
# when we miss to write the ending index then it will take the value of last index and will print till the end of the string

subString = name[0:3]
print(subString) # Div

# to print the character from the string 
index0 = name[0]
print(index0) # D
index1 = name[1]
print(index1) # i


# to print by skipping index multiple values
# like the value is 2 .. hence it will make jumps of 2
new = name[0:7:2] # skip the 2 multiple index
print(new) # Dvas
