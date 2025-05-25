# to take input of eight numbers and displays only unique of them

s = set()

s.add(int(input("Enter the number : ")))
s.add(int(input("Enter the number : ")))
s.add(int(input("Enter the number : ")))
s.add(int(input("Enter the number : ")))
s.add(int(input("Enter the number : ")))
s.add(int(input("Enter the number : ")))
s.add(int(input("Enter the number : ")))
s.add(int(input("Enter the number : ")))


print(s)

# checking if a set can hold integer and string of same value
# yes possible 

set1 = {3,"3"}
print(set1)

# getting the length of a set

set2 = set()

set2.add(20)
set2.add(20.0)
set2.add('20')

print(len(set2))
# the length will be 2 it will take 20 and 20.0 equal 
# in case of python int and float are equal 


