## in this we are writing the table for every value of n and making a file for it ,, in which the value resides

def func(n):
    table = ""
    for i in range(1 , 11):
        table += f"{n} * {i} = {n*i}\n"
    return table
    

for i in range(2,21):
    with open(f"table{i}.txt","w") as f:
        f.write(func(i))