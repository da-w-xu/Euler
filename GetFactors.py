from math import sqrt

def GetFactors(n):
  factors=[]
  for i in range(1,sqrt(n+1),1):
    if n%i==0:
      factors.append(i)
      factors.append(n/i)
  return factors
