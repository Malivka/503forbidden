
# Q2: File processing
# input file format: name m1 m2 m3 m4 m5

inp = open("students.txt", "r")
out = open("passed.txt", "w")

for line in inp:
    data = line.split()
    name = data[0]
    marks = []
    for i in range(1,6):
        marks.append(int(data[i]))
    total = 0
    for m in marks:
        total += m
    percent = total/5
    if percent >= 60:
        out.write(name + " " + str(total) + " " + str(percent) + "\n")

inp.close()
out.close()

# read output file and find highest and average
f = open("passed.txt", "r")
percs = []
for line in f:
    p = float(line.split()[2])
    percs.append(p)

if len(percs) > 0:
    high = percs[0]
    s = 0
    for x in percs:
        s += x
        if x > high:
            high = x
    print("Highest %:", high)
    print("Average %:", s/len(percs))
else:
    print("No students >=60%")
f.close()
