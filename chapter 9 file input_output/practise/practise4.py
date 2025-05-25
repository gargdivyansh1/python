## when only one word is need to be replace
# here we will first fetch the data of the file .. and then we will replace the required word by using the replace method and then we will write it into the same file again .. this how it will change the data to the required data 

word = "donkey"

with open("donket.txt","r") as f:
    content = f.read()

# replace is used to replace an existing data to new data

contentNew = content.replace(word,"#####")

with open("donket.txt","w") as f:
    f.write(contentNew)





# when a list of word is need to be replace 

ls = ["Donkey","Divyansh","Diksha"]

with open("hello.txt","r") as f:
    content = f.read()

# using the loop and replacing for each word and then writing it as usual
for item in ls:
    content = content.replace(item,"#####")

with open("hello.txt","w") as f:
    f.write(content)