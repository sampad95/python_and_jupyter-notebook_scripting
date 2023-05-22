# Fibonacci series with x_0 = 0 and x_1 = 1

n=eval(input('Enter the value of n\n'))

def rec_fib(x_n):
  if x_n <= 1:
    return x_n
  else:
    return(rec_fib(x_n-1) + rec_fib(x_n-2))

if n <= 0:
  print("Invalid input ! Please input a positive value greater than or equal to one")
else:
  print('Fibonacci series for n=',n,':')
#   for i in range(n+1):
#       print(rec_fib(i))
  print([rec_fib(i) for i in range (n+1)])
