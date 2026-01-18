
n=int(input("Enter number: "))
if n<=1:
    print("Not prime")
else:
    prime=True
    for i in range(2,n):
        if n%i==0:
            prime=False
            break
    if prime:
        print("Prime")
    else:
        print("Not prime")
