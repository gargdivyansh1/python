# there are various methods in tuple 

num = (1,2,3,4,5)

# it can also take multiple data types in single tuple
num2 = (3, "odfs", 'd')

for i in num2:
    print(i)

# 1. to count the number of occurance of any value in the tuple 
print(num.count(2))

# 2. return the first occurance of any value 
# remember if a number is repeating more then one time in the tuple then it will give the index of first occuring only 
print(num.index(3)) # here we pass the value and then get the index in return 

# 3. concatinating two tuples 
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
print(tuple1 + tuple2)

# 4. checking if the value is present on not in the tuple 
print(2 in num)
print(6 in num)
# like if you don't know this thing for checking if the value is in the tuple or not 
# then you can use count functon if the value is 0 then it is not present in the tuple

# 5. itereating through a tuple 
# print all the value one by one 
for i in num:
    print(i)