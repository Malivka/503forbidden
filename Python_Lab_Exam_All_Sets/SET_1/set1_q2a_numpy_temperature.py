
import numpy as np
temps = np.array([30,32,31,29,35,34,33])
avg = np.mean(temps)
count = 0
for t in temps:
    if t > avg:
        count += 1
print("Average:", avg)
print("Days above average:", count)
