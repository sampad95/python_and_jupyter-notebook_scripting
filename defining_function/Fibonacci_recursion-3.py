# Fibinacci series with x_0 = 1 and x_1 = 1

x_n=eval(input('Enter the position x_n\n'))

def rec_fib(x_n):
  if x_n <= 1:
    return 1
  else:
    return(rec_fib(x_n-1) + rec_fib(x_n-2))

print('The', x_n,'th Fibonacci number is:',rec_fib(x_n))
