
## printing pattern 

#    *
#   ***
#  *****

## here by multipling we can print same thing many times

n = int(input("Enter number of rows: "))
m = int(input("Enter number of columns: "))


for i in range(1,n+1):
    print(" "* (n-i),end="")
    print("*"* (2*i-1),end="") # we use end="" for not auto moving next line
    print("\n")


# *
# **
# ***

for i in range(1,n+1):
    print("*"*i,end="")
    print("\n")

# * * *
# *   *
# * * *

for i in range(1,n+1):
    if(i==1 or i==n):
        print("*"*m,end="")
    else:
        print("*",end="")
        print(" "*(m-2),end="")
        print("*",end="")
    print("\n")


# by default the print statement after execution break the line and make the pointer in the next line 