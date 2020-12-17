def fibonacci(n):
  if n == 0 or n == 1:
    return n
  fib_table = [0, 1]
  fib = 1
  for i in range(2, n + 1):
    fib = fib_table[1] + fib_table[0]
    fib_table[0] = fib_table[1]
    fib_table[1] = fib
  return fib
  
