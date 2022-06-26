n=eval(input('Enter the integer upto which you want to do sum\n'))
s=0
for i in range(1,n+1):
    s=s+i
print('sum=',s)

#or

print('Sum=',sum(range(1,n+1)))   # sum is in-built function
