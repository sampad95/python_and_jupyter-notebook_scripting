def fact(n):
    fact=1
    for i in range(2,n+1):                 
        fact=fact*i
    return fact

n=eval(input('Enter the value of n\n'))
print(fact(n))
