x = 300
y = 300
c = 300
k = 300
g = 300
n = 300
def setup():
  size(600,600)
  frameRate(10) 
def draw():
  global x,y,c,k,g,n
  background(10)
  strokeWeight(300)
  fill(random (0,255),random (0,255),random (0,255))
  stroke(random (0,255),random (0,255),random (0,255))
  ellipse(300,300, y,y)
  ellipse(20,20, x,x)
  ellipse(580,580, y,y)
  x = x + 100
  y = y - 100
  c = c - 9
  k = k + 1
  n = n + 1
  g = g + 1

  
