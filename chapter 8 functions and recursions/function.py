# function definition 

def avg():
    a = int(input("Enter first number : ")) 
    b = int(input("Enter second number : "))
    c = int(input("Enter third number : "))
    d = int(input("Enter fourth number : "))
    e = int(input("Enter fifth number : "))
    f = int(input("Enter sixth number : "))

    average = (a+b+c+d+e+f)/6
    print(average)

# function calling 
avg()



# function with arguments 

# here this function is not returning any value
def goodDay1(name):
    print(f"Good Day {name}")

goodDay1("Divyansh")


# here this function is returning the value which could be assigned to a variable and could be used as result
def goodDay2(name):
    a = "Good Day " + name
    return a 

a = goodDay2("Divyansh")
print(a)



# default argument in function 
# when we didn't pass the argument so it take the default value

# here the value of ending which is provided is the default value
# when the user didn't provide this .. then it will take this value otherwise the value provided by the user will be taken
def goodDay3(name , ending="Thank You"):
    print(f"Good Day, {name}", end=" ")
    print(ending)

goodDay3("Divyansh", "Thanks") # here we have pass the value of argument 
                              # hence it will take value which we have given

goodDay3("Diksha") # here we haven't given the value of the argument hence take the default value















