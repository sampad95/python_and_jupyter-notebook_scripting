def sum(n):
    sum=0
    for i in range(0,n+1):                                # takes values upto n starting from 0
        if i%2==0:
            sum=sum+i
    return sum
n=eval(input('Enter the number upto which you want to sum up\n'))
print(sum(n))
