
# name formatting
f=input("First: ")
m=input("Middle: ")
l=input("Last: ")
print("Name:", l.capitalize()+", "+f.capitalize()+" "+m.capitalize())

# designation
des={"a":"Professor","b":"Associate Professor","c":"Assistant Professor","d":"Sr Lab Technician","e":"Jr Lab Technician"}
ch=input("Enter designation code: ")
print("Designation:", des.get(ch,"Invalid"))

# leap year
y=int(input("Enter year: "))
if (y%400==0) or (y%4==0 and y%100!=0):
    print("Leap year")
else:
    print("Not leap year")
