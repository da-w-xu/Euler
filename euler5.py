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

def GetPrimeFactors(x):
  x = abs(int(x))
  factors = []
  if IsPrime(x) == True:
    factors.append(x)
    return factors
  
  for a in xrange(2,int(sqrt(x))+1,1):
    if x % a == 0:
      if IsPrime(a):
        factors.append(a)
      else:
        factors.extend(GetPrimeFactors(a))
    
      factors.extend(GetPrimeFactors(x/a))
      return factors
  return factors

primeFactors = []
for i in range(2,50):
  primes = GetPrimeFactors(i)
  for p in primeFactors:
    if (p in primes):
      primes.remove(p)
  primeFactors.extend(primes)

print primeFactors
finalNumber = 1
for a in primeFactors:
  finalNumber *= a
print finalNumber

