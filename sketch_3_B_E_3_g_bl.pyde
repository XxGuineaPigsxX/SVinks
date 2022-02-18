def setup():
    size(600,400)
    background(10)
    
    
    frameRate (20)
def draw():
    translate(300,200)
    stroke (random(0,255),random(0,255),random(0,255))
    strokeWeight (random(2,8))
    point(random (-300,300),random (-200,200))
    
    
