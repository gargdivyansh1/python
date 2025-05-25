# we can access others files and also other things in our program 

# to write in the file 

f = open("newfile.txt","w")
value = input("Enter the data which you want to write into the file: ")
f.write(value)
f.close
# here we are writing which means the data written in the file will be changed to this data .. here we are not updating 
# for that we could use the append mode instead of the writing mode



# to read a file 

f = open("newfile.txt","r")
data = f.read()
print(data)
f.close()
# here is a situation arises that the file which you want to read is not present 
# then for the safer side made the file first .. if it alredy present then no file will be made if the file is not present then the file will be made having no data ... then do not show any result when you read it .. otherwise it will error if no file found which such name




# f.readline is used to read a line of a paragraph 
# f.readlines is used to read all lines of a paragraph
