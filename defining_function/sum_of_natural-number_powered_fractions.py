def sum(x,n):
    """This is the infinite series sum of 1/x^n"""
    sum=0
    for i in range(0,n+1):                                # takes values upto n starting from 1
        sum=sum+(1/x**i)
    return sum
x=eval(input('Enter the value of x\n'))
n=eval(input('Enter the value of power upto which wnat to get the number\n'))
print(sum(x,n))
print(sum.__doc__)
