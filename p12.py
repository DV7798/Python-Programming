def fact(n):
    f=1
    while n>=1:
        f=f*n
        n-=1
    return f

n=int(input('Enter the number '))
f=fact(n)
print('Factorial is',f)
