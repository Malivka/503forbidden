
lst = [10,5,20,8,15]
largest = lst[0]
second = -10**9
for x in lst:
    if x > largest:
        second = largest
        largest = x
    elif x > second and x != largest:
        second = x
print(second)
