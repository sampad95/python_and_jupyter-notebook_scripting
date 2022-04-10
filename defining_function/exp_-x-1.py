def sum(x,n):
    """This is exp(-x) infinite series sum"""
    sum=0
    def fact(n):                       # function inside a function
        """Factorial function inside exp(-x) infinite sum function"""
        fact=1
        for i in range(1,n+1):
            fact=fact*i
        return fact
    print(fact.__doc__)      # prints about the factorial function written inside triple quotes inside the function definition
    for j in range(0,n+1):
        sum=sum+(((-1)**j)*(x**j)/fact(j))
    return sum
print(sum.__doc__)               # prints about the sum function written inside triple quotes inside the function definition
x=eval(input('Enter the value of x\n'))
n=eval(input('Enter the value of n\n'))
print(sum(x,n))
