import math
def f(x):
  return math.exp(-x)

def taylor(n, x, a):
  return f(a) * (-1)**n * (x-a)**n / math.factorial(n)

def suma(n, x, a):
 
  sum = 0
  
  for i in range(n+1):
    
    sum += taylor(i, x, a)

  return sum


x = 0.505
a = 0.5

for n in range(16):
  
  estimate = suma(n, x, a)
  
  errorAp = abs((f(x) - estimate) / f(x)) * 100
  
  print(f"La estimación de orden {n} es {estimate}. El error es {errorAp}%")