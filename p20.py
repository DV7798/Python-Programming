s = input('Enter the String: ')
add = input('Enter the String to be added: ')
n=int(input('Enter the position where you want to add the string: '))

res = s[ : n] + add + s[n : ] 

print("The string after performing addition : " + str(res)) 