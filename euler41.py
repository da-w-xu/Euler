from IsPrime import *
from IsPandigital import *

def Euler41(n):
  while n>0:
    l = sorted(GetPandigitals(n))
    l.reverse()
    for i in l:
      if IsPrime(i):
        print i
        return
    n-=1

Euler41(9)
