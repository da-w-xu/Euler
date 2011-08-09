from math import sqrt
import GetFactors

def GetTriangleN(n):
  n = int(abs(n))
  if n%2 == 0:
    return (n+1)*(n/2)
  else: 
    return (n+1)*((n-1)/2)+(n+1)/2

def Euler12():
  n=0
  x=0
  while 1:
    n+=1
    x=GetTriangleN(n)
    factors=GetFactors.GetFactors(x)
    if len(factors) > 500:
      break
    #print x,len(factors)
  print x

Euler12()
