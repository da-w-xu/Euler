

def euler20():
  n=99
  total=100
  while (n>0):
    total *= n
    if total%10 == 0:
      total /= 10
    n-=1
  print sum(map(int,str(total)))

euler20()
