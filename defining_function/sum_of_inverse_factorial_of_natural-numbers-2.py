def sum(n):
    sum=0
    def fact(n):                       # function inside a function
        fact=1
        for i in range(1,n+1):
            fact=fact*i
        return fact
    for j in range(1,n+1):
        sum=sum+(1/fact(j))
    return sum
n=eval(input('Enter the value of n\n'))
print(sum(n))
