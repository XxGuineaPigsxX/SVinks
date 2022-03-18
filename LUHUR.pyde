x = 0
def setup():
    size(400,400)
    translate(200,200)
    frameRate(100000000000000000)
def draw():
    global x
    strokeWeight(10)
    stroke(random(0,255),random(0,255),random(0,255))
    translate(200,200)
    rotate(radians(x))
    ellipse(0,0,200,1)
    x = x + 1

    
