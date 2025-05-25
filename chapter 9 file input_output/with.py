# f = open("file.txt")
# print(f.read())
# f.close()

# instead of writing f.close again and again we can use a different thing 
# which is with thing 

with open("file.txt") as f:
    print(f.read())
