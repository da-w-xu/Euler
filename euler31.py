import sys

coins = [1,2,5,10,20,50,100,200]

def Euler31(left, last):
  if last>left:
    last=left 
  if left==0:
    return 1
  if left<0:
    return 0
  if last==1:
    return 1 #only 1 path for remaining coins to take: pennies
  
  paths=0
  for i in coins:
    if i<=last:
      paths+=Euler31(left-i,i)
  return paths


#####
if len(sys.argv)==2:
  print Euler31(int(sys.argv[1]),200)
else:
  print Euler31(31,200)
