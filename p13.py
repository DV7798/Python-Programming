def prime(n):
    c=0
    for i in range(2,n):
        if(n%i==0):
            c+=1
    if c<2:
        print("Prime Number")
    else:
        print("Not a Prime Number")

n=int(input("Enter the number :"))
prime(n)