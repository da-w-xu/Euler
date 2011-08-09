import itertools

def GetPandigitals(n):
  """ Get all pandigitals with len n """
  l = list( itertools.permutations(range(1,n+1)) )
  p = []
  for i in l:
    x = 0
    for k in i:
      x *= 10
      x += k
    p.append(x)
  return p

def IsPandigital(n):
  n = int(n) 
  l = len(str(n))
  panset = []
  for i in range(10):
    panset.append(False)
  
  while n>0:
    r = n%10
    if r==0: 
      return False
    r -= 1
    if panset[r]==False:
      panset[r]=True
    else:
      return False
    n = n/10

  for i in range(l):
    if panset[i] == False:
      return False
  return True
