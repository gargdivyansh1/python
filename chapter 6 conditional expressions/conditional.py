# getting knowledge about if and elif and else

a = int(input("Enter your age : "))

# if elif else ladder 

if(a>=18):
    print("You are eligible.")
    print("Good for you")
elif(a<0):
    print("You are entering an invalid age ")
elif(a<18):
    print("You are not eligible")
elif(a==0):
    print("You are below the age of consent ")

print("End of program")