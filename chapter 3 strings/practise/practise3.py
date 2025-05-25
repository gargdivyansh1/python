# stringname.find(value) is used for finding the value and returns the index of it 
# the indexing will start from 0
# remember it will only return the first occuring of the value if there are multiple occurences of the value
# if the value is not found it will return -1 

name = "divyansh"
print(name.find("v"))

# try for detecting double spaces in strings
name1 = "Here is        your  string"
print(name1.find("  "))

# replacing the 8 spaces with single spaces 
print(name1.replace("        "," "))

# replacing the double spaces with single space
print(name1.replace("  "," "))