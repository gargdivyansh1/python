# calculate the sum of first n natural numbers

def sumfun(n):
    if(n==1):
        return 1
    return n + sumfun(n-1)


a = int(input("Enter a number: "))

print(f"The sum of {a} natural numbers is {sumfun(a)}")