# to take input of name as key and also the values 

d = {} 

name = input("Enter the name : ")
value = input("Enter the language : ")
d.update({name:value})

name = input("Enter the name : ")
value = input("Enter the language : ")
d.update({name:value})

name = input("Enter the name : ")
value = input("Enter the language : ")
d.update({name:value})

name = input("Enter the name : ")
value = input("Enter the language : ")
d.update({name:value})

name = input("Enter the name : ")
value = input("Enter the language : ")
d.update({name:value})

print(d)

############## important point to remember ############## 
# if there are two keys of same name and different values
# then the program will take the value which comes later 
# as we are using the updatge function

# like "divyansh" : "python"
#      "divyansh" : "c"
# then it will take the value as c
