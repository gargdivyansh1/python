## checking if the file data contain the specific word or not

with open("log.txt","w") as f:
    s = "Hello "
    f.write(s)

with open("log.txt","r") as f:
    content = f.read()
    if("python" in content):
        print("Yes")
    else:
        print("No")