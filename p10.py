def greatest(a,b,c):
    if a>b and a>c:
        return a
    elif b>c:
        return b
    else:
        return c
print('Enter 3 nos')
a=int(input())
b=int(input())
c=int(input())
print('Greatest is',greatest(a,b,c))