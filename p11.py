print('Enter the coefficients of the quadratic equation ')
a,b,c=input().split()
a,b,c=int(a),int(b),int(c)
d=b*b-4*a*c
d=d**(1/2)
r1=(-b+d)/(2*a)
r2=(-b-d)/(2*a)
print('roots are ',r1,r2)