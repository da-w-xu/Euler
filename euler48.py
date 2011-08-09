def LastTenPower(n):
  x=n
  for i in range(1,n):
    x*=n
    x=x%10000000000
  return x

sum=0
for k in range(1,1001):
  sum+=LastTenPower(k)

print sum
