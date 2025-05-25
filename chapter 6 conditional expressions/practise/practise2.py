# to check weather the string is talking about you or not

post = input("enter your post: ")

finding = input("Enter the name to find: ")

# by doing the letters to lower case you could able to find the word irrespective of its casee

if(finding.lower() in post.lower()):
    print("Ya content is here")
else:
    print("Content is not here")   
    
# making everthing into a single case is a good practice for checking as is the string contain the value but in the different case .. then we want it to give yes ... hence convert it into single case and then check
