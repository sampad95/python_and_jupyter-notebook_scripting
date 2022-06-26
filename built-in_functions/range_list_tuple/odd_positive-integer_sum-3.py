m=eval(input('Enter the starting odd positive integer\n'))
n=eval(input('Enter the odd positive integer upto which you want to do sum\n'))
s=0
for i in range(m,n+1,2):
    s=s+i
print('sum=',s)

#or

print('Sum=',sum(range(m,n+1,2)))   # sum is in-built function
