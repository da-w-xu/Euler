def IsPalindrome(n):
  n = int(n)
  strN = str(n)
  first = 0
  last = len(strN)-1
  while first < last:
    if strN[first] != strN[last]:
      return False
    first+=1
    last-=1
  return True  

largest = 0
for i in range(100,999):
  for j in range(i,999):
    if IsPalindrome(i*j) and (i*j)>largest:
      largest = i*j

print largest
 

