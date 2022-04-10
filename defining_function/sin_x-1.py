def sum(x,n):
    sum=x
    def fact(n):                       # function inside a function
        fact=1
        for i in range(1,n+1):
            fact=fact*i
        return fact
    for j in range(1,n+1):
        sum=sum+((((-1)**j)*(x**((2*j)+1)))/fact((2*j)+1))
    return sum
x=eval(input('Enter the value of x\n'))
n=eval(input('Enter the value of n\n'))
print(sum(x,n))
