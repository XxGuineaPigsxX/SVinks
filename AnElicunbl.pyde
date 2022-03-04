x = 300
y = 300
c = 300
k = 300
g = 300
n = 300
def setup():
  size(600,600)
def draw():
  global x,y,c,k,g,n
  background(100)
  ellipse(x,x, 50,50)
  ellipse(y,y, 50,50)
  ellipse(x,y, 50,50)
  ellipse(y,x, 50,50)
  x = x + 1
  y = y - 1
  c = c + 1
  k = k + 1
  n = n + 1
  g = g + 1

  
