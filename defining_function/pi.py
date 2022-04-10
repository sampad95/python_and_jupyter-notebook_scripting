def sum(n):
    sum=0
    for i in range(1,n+1):
        sum=sum+(((-1)**(i+1))*(1/((2*i)-1)))
    return sum
n=eval(input('Enter the value of n\n'))
print('pi/4=',sum(n))
print('pi=',4*sum(n))
