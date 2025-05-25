# way of storing the multiple data 
# like array
# unlike strings lists are mutable  

friends = ["Ram" , "Shyam"]
dads = ["Divyansh", "Dibbi", "Kalia"]
sons = []

for i in dads:
    print(i)

# we can also replce the value at any index
friends[0] = "Timmy"
# now the first value of the list will be changed to Timmy 

print(friends[0])
print(friends[0:2]) # this will work same as the string indexing and slicing 

for i in friends:
    print(i)    


# this will give the error as the list is empty 
# sons[0] = "baby"

# for i in sons:
#     print(i)