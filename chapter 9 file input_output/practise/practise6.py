## to make a copy of a file in another file
 
# original
with open("original.txt") as f:
    content = f.read()

# copy
with open("copy.txt","w") as f:
    f.write(content)



## to check weather a file is identicial or not 


# here we are not providing the mode in which we are opening the file .. hence default is read mode 'r'
with open("original.txt") as f:
    content = f.read()

with open("copy.txt") as f:
    content1 = f.read()

if(content == content1):
    print("Yes they are identicial")
else:
    print("They are not identicial")



## to wipe out the content of the file 

# we will write noting this will replace the old content to the nothing
with open("newfile.txt","w") as f:
    f.write("")