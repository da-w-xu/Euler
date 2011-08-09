from math import sqrt

def IsPrime(x):
  x = abs(int(x))
  if x < 2:
    return False
  if x == 2:
    return True
  if not x & 1:
    return False
  
  for a in xrange(3,int(sqrt(x))+1,2):
    if x % a == 0:
      return False
  return True
