# print table with multiplication showing 

n = int(input("Enter the number: "))

# for straight order
for i in range(1,11): ## here we have used 1 to start range from 1 , as it starts from 0 
    print(f"{n} * {i} = {n*i}")

#for reverse order 
m = 10 

for i in range(1,11): ## here we have used 1 to start range from 1 , as it starts from 0 
    print(f"{n} * {m} = {n*m}")
    m-=1

## checking of prime numbers 

n = int(input("Enter the number: "))

for i in range(2,n):
    if(n%i) == 0:
        print("Not a prime")
        break
else:
    print("prime")


## remember we can also use else in for loop 