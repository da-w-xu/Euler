from sets import Set
from math import sqrt

max = 28124

def GetFactors(n):
  n = int(abs(n))
  factors =Set([])
  for i in range(1,int(sqrt(n))+1):
    if n%i==0:
      factors.add(i)
      factors.add(n/i) 
  return factors

abundant = []

# construct abundant list
for i in range(1,max):
  factors = GetFactors(i)
  factors.remove(i)
  sum=0
  for k in factors:
    sum+=k
  if i<sum:
#    print factors, i
    abundant.append(i)

# construct 2 abuandant sum list
sumSet = Set([])
for i in abundant:
  for j in abundant:
    sumSet.add(i+j)
    

finalSum=0
for i in range(1,max):
  if not (i in sumSet):
    finalSum += i

print finalSum

# find numbers that cannot be added by two abundant numbers
#for i in range(1,max):
#  start=0
#  end=len(abundant)-1
#  while 1:
#    if start>end:
#      finalSum+=i
#      break
#    sum = abundant[start]+abundant[end]
#    if sum==i:
#      break
#    elif sum>i:
#      end-=1
#    elif sum<i:
#      start+=1
   
print finalSum 
