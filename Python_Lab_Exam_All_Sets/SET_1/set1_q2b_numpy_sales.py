
import numpy as np
sales = np.array([[10,20,30],[5,15,10],[25,5,5]])
totals = []
for row in sales:
    s = 0
    for x in row:
        s += x
    totals.append(s)

maxi = totals[0]
idx = 0
for i in range(len(totals)):
    if totals[i] > maxi:
        maxi = totals[i]
        idx = i

print("Totals:", totals)
print("Highest selling product index:", idx)
