# writing a program in which we are replacing the values 

letter = '''Dear <|Name|> ,
You are selected!
<|Date|>'''

# here we have to replace name and date
# we can use the replace function to do this

c = letter.replace("<|Name|>","Divyansh")
d = c.replace("<|Date|>","26 feb")

# as the format of the letter is using the three single quotes this means the structure of the letter will not be disturbed
print(d)