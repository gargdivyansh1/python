# remember lists are mutable unlike strings 
# means if you made any change in the lists and then print 
# then the new value lists would print 

# the list could contain any type of data in one same list only
friends = ["Apple" , "Orange" , 5 , 345.06 , False , "Aakash" , "Rohan", "Divyansh", "Divyansh"]

print(friends)

# to join the value in the right most place
friends.append("Divyansh")
print(friends)

# for sorting of lists 
num = [1,5,3,645,324,256,9]
num.sort()
print(num)

# to reverse a list 
friends.reverse()
print(friends)

# inserting at a particular index 
friends.insert(2, "HELLO")
# this will add HELLO at the 2 index 
print(friends)

# removing a particular index value 
friends.pop(2)
#this will pop index value 
print(friends)

# this will only remove the first occurance of the value from the list 
# to remove the required value
friends.remove("Divyansh")
# this will remove the divyansh from the list 
print(friends)