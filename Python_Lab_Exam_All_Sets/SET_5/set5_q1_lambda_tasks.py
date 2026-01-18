
nums=[1,2,3,4,5,2,3,4]

# remove duplicates
unique=[]
for x in nums:
    if x not in unique:
        unique.append(x)
print(unique)

# odd numbers
odds=list(filter(lambda x:x%2!=0, unique))
print("Odds:", odds)

# cubes
cubes=list(map(lambda x:x**3, odds))
print("Cubes:", cubes)

# sum of cubes
s=0
for x in cubes:
    s+=x
print("Sum:", s)
