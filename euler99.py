from math import log

def euler99():
  f = open('base_exp.txt','r')
  maxN=0
  maxLine=1
  lineNum=1
  for line in f:
    b,e=line.split(',')
    b=int(b)
    e=int(e)
    if e*log(b) > maxN:
      maxN=e*log(b)
      maxLine=lineNum
    lineNum+=1
  print maxLine

euler99()
