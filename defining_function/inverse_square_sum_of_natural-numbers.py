def sum(n):
    sum=0
    for i in range(1,n+1):                                # takes values upto n starting from 1
        sum=sum+(1/i**2)
    return sum
n=eval(input('Enter the value of n\n'))
print(sum(n))
