def fib(n):
    a,b=1,1
    c=a+b
    print(str(a)+","+str(b)+","+str(c),end="")
    while c<n:
        print(","+str(c),end="")
        a=b
        b=c
        c=a+b
n=int(input("Enter the number "))
fib(n)