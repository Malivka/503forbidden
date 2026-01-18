
lst = [1,2,3,2,4,1,5]
res = []
for x in lst:
    if x not in res:
        res.append(x)
print(res)
