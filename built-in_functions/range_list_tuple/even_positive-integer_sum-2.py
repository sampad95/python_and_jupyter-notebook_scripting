m=eval(input('Enter positive integer\n'))
print('start value is',2*m)
n=eval(input('Enter positive integer\n'))
print('stop value is',2*(n+1))
s=0
for i in range(m,n+1):
    s=s+(2*i)
print('sum=',s)

