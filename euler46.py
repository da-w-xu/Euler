from IsPrime import IsPrime
from math import sqrt

primes = [2]

def IsPerfectSquare(n):
  x = sqrt(n)
  x = int(x)
  if x*x==n:
    return True
  else: return False

def Euler46():
  i=3
  while 1:
    if IsPrime(i):
      primes.append(i)  
    else:
      # check conjecture, all primes + some 2*k^2 == i?
      found=False
      for p in primes:
        n = (i-p)/2
        if IsPerfectSquare(n):
          found=True
          #print 'break for i: ',i,' p: ',p,' n: ',n
          break
      if found==False:
        print 'found Goldman #: ',i
        exit()
    i+=2
    #if i%10000==1: print i

Euler46()
