# properties of dictionary 

# it is un-ordered 
# it is immutable 
# it is indexed 
# cannot contain duplicate keys

# learn some new methods in dictionary by chatgpt

# d = {} empty dictionary 


marks = {
    "Anushka": 100,
    "Diksha": 90,
    "Divyansh": 105
}

print(marks) # to print the whole dictionary 
print(marks["Divyansh"]) # to print the value of the key 

# to get the keys
print(marks.keys())

# to get the values 
print(marks.values())

# to get the all items 
print(marks.items())

# we can update the values of keys 
marks.update({"Anushka": 99}) # this will change the 100 to 99
print(marks)

# and if we want to update the dictionary with new keys then
# also we can use update 
# add the value in the last 

# hence Anu is not present in the dictionary then it will add the key Anu with value 100
marks.update({"Anu":100})
print(marks)

# to get the value of the specific key 
print(marks.get("Anu")) # this will give none if the key is not present 
print(marks["Anu"]) # this will give error if the key is not present

# the difference in these two is that 
# if the key is not present in the dictionary 
# then get function will give the value none while square bracket will give error 

# to get the length of the dictionary 
print(len(marks))

# to delete any key from the dictionary
marks.pop("Divyansh")
print(len(marks)) # this will give the length of the dictionary after deleting the key
print(marks)