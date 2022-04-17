def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)

n=eval(input('Enter the value\n'))
print(n,'!=',fact(n))
