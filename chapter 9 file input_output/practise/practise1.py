# first make a file containing a poem 

with open("poems.txt","w") as f:
    f.write("""In the hush of morning light,
Dreams still linger, soft and bright.
Hope begins with whispered grace,
Smiling in the sun’s embrace. """)
    f.close()

# now add a poem in it 

with open("poems.txt","r") as f:
    content = f.read()
    print(content)
    if("soft" in content): ## this is used to check the word 
        print("YES")
    else:
        print("no")

    

# f = open("poems.txt")
# content = f.read()
# if("hello" in content):
#     print("Yes")
# else:
#     print("no")