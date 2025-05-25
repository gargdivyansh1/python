# sets are used to hold only values not keys

# to create an empty dictionary 
# a = set()
# a = {} -> it will create empty dictionary 

# we can not repeat elements in set 
# a = {1,54,56,73,73,4} # it will take 73 only one time

s = {1,5,32,54,5,5,5,"Divyansh"} # only take 5 one time 
print(s)

# we can also add values in the set 
s.add(34)
print(s)

# methods 
# a triangle b equal to the union of A and (A-B)
# means A + (A-B) as union is like addition of two sets and set does not contain duplicate hence will remove the same values

# 1. len(set) to get the length of set 
# 2. set.add(value) to add the value
# 3. set.remove(value) to remove the desired value and update set
# 4. union to join to set 
# 5. intersection to take the intersection of the sets 

set1 = {1,2,3,4}
set2 = {5,6,7,4,8}

print(set1.union(set2))
print(set1.intersection(set2))