
studentIDs=[201,202,203,204,205,206,207]
scores=[85,92,78,64,88,91,73]

# IDs with score >=75
res=[]
for i in range(len(scores)):
    if scores[i]>=75:
        res.append(studentIDs[i])
print("Eligible IDs:",res)

# average score
s=0
for x in scores:
    s+=x
print("Average:", s/len(scores))

# lowest score student
low = scores[0]
idx = 0
for i in range(len(scores)):
    if scores[i] < low:
        low = scores[i]
        idx = i
print("Lowest score ID:", studentIDs[idx])
