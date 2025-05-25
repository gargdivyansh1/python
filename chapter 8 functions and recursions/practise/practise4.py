# program to remove a item from a list 

def program(l , word):
        l.remove(word)
        return l
    

l = ["Divyansh" , "Ponting" , "Richi", "Ponting"]

print(program(l,"Ponting"))
# if we directly use the remove method then it will only remove the first occurane 
# here also the function is using the remove hence it will also remove the first occurance only 
# to remove all the occurance use the count method which will give you count of each word .. and then use the remove method the number of times the count value of the word which you want to remove -- a very intutive way ,,, many other faster ways are possible





# good question learn it now only 

# here is a program for removing the desire word 
# and also strip other words 

# strip means to remove the given letters from the word

# here in this function we are checking each word .. if the word is equal to the word passed in the parameters then we are not adding it into the list .. but if the word does not match then we are adding it by removing the desired letters from it .. which is called stripping and for that we are using the method strip

def program1(l,word):
    n = []
    for i in l:
        if (i!=word):
            n.append(i.strip(word))
    return n    

l = ["Divyansh" , "Ponting" , "Richi" , "an" , "higan"]

print(program1(l,"an"))