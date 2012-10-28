from math import sqrt

def IsTriplet(a,b,c):
  if a*a+b*b==c*c:
    return True
  return False

def TripletsEqualTo(a,b,c,n):
  if a+b+c==n:
    return True
  return False

def Euler9():
  #c_max = int(sqrt(1000))
  c_max=1000
  print 'euler9! cmax:', c_max
  for c in range(0,c_max+1):
    for b in range(0,c-1):
      for a in range(0,b-1):
        if IsTriplet(a,b,c):
          #print 'found a triplet:',a,b,c
          if TripletsEqualTo(a,b,c,1000):
            print a,b,c
            return

def Euler9_b():
  # construct map of A^2+B^2. Then just find 1000-N==C^2.

Euler9()
