# write a program to sum a list of four numbers 

num = [1,2,3,4]

# sum is a function which gives the sum of the values of list 

# here we are using the sum function for taking the sum of the values in the list
print(sum(num))

# but we can also use the for loop and we will iterate through it and sum in the external variable
sum = 0 
for i in num:
    sum += i 

print(sum)




