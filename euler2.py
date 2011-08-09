
def NextFib(first, second):
  return first+second

sum = 2
fib1 = 1
fib2 = 2
fibNext = NextFib(fib1,fib2)
while (fibNext<4000000):
  fib1 = fib2
  fib2 = fibNext
  if (fibNext%2 == 0):
    sum += fibNext
  fibNext = NextFib(fib1,fib2)

print sum
