# *
# **
# ***
n=int(input('Enter value of n'))
for i in range(0,n):
    for j in range(0,i+1):
        print('*',end="")
    print()
# 1
# 12
# 123
for i in range(0,n+1):
    for j in range(1,i+1):
        print(j,end="")
    print()
#   * 
#  * * 
# * * *
for i in range(0,n):
    for j in range(0 , n - i):
        print(" ",end="")
    for j in range(0, i + 1): 
        print("* ",end="")
    print()
#   1
#  22
# 333
for i in range(0,n):
    for j in range(0 , n - i):
        print(" ",end="")
    for j in range(0, i + 1): 
        print(i+1,end="")
    print()