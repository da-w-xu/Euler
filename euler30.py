import sys

def Euler30(power):
  if power<1:
    return
  # construct dict so we don't keep calculating pow(x,y)
  d = {}
  for i in range(0,10):
    d[i] = pow(i,power)

  # establish upper bound for brute force search
  i=1
  while i*d[9] > pow(10,i):
    i+=1
  maxN = (i-1)*pow(9,power)

  # find euler30 numbers
  for i in range(2,maxN):
    total=0
    istr = str(i)
    for j in range(0,len(istr)):
      total+=d[int(istr[j])]
      if total>i:
        continue
    if total==i:
      print i

if len(sys.argv) != 2:
  print "usage:\npython "+sys.argv[0]+" #"
else:
  Euler30(int(sys.argv[1]))

  
