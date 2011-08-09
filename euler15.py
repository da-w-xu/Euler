d = dict({'1,1': 2,'2,2': 6,'3,3': 20})

def Grid(x,y):
  #sort x,y
  if x>y:
    t=x
    x=y
    y=t

  #check dictionary
  l=`x`+','+`y`
  if l in d:
    return d[l]

  #return Nx1 
  if x==1 or y==1:
    return x+y

  #
  if x==y:
    z = 2*Grid(x-1,y)
    d[l]=z
    return z

  z = Grid(x-1,y)+Grid(x,y-1)
  d[l]=z
  return z

print Grid(500,500)
