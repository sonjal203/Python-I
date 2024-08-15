n=int(input("Enter number: "))
k=0
for i in range(2,n//2+1):
    if(n%i==0):
        k=k+1
if(k<=0):
    print("Number is prime")
else:
    print("Not a Prime Number")


