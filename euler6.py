def SumSquaresFirstN(n):
  sum=0
  for i in range(1,n+1):
    sum += i*i
  return sum

def SquareSumsFirstN(n):
  sum=0
  for i in range(1,n+1):
    sum += i
  sum *= sum
  return sum

print SquareSumsFirstN(100)-SumSquaresFirstN(100)

