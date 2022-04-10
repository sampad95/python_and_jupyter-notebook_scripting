def sum(n):
    sum=0
    for i in r:                                # takes values upto n starting from 1
        sum=sum+i
    return sum
n=eval(input('Enter the value of n\n'))
r=range(1,n+1)
print(sum(n))

