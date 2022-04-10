def sum(n):
    sum=0
    for i in range(1,n+1):                                # takes values upto n starting from 1
        sum=sum+(2*i)
    return sum
n=eval(input('Enter how many numbers do you want to sum\n'))
print(sum(n))
