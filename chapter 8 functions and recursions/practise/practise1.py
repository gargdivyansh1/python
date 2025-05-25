# to find the greatest of three numbers

def greatest(a,b,c):
    if(a>b):
        if(a>c):
            return a
        else:
            return c
    elif(b>a):
        if(b>c):
            return b
        else:
            return c    
    elif(a==b):
        if(a>c):
            return a
        else:
            return c 
        


a = greatest(13,43,532)
    
print(a)