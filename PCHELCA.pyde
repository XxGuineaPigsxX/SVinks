x=0 
n=-1
m=0
b=-1
fillVal = 0
HAnpoBLeHue="право"  
HAnpoBLeHue2="право"  
def setup():
    size(1000,600)
    frameRate(120)

def draw():
    
    background(217,245,252)
    global x,HAnpoBLeHue,n,HAnpoBLeHue2
    fill(254,255,0)
    push()
    translate(x,0)
    scale(n,1)
    rect(-60,300,100,50)
    fill(102,138,196)
    ellipse(10,280,30,50)
    strokeWeight(10)
    rect(-10,300,1,50)
    rect(10,300,1,50)
    point(-30,320)
    pop()
    
    push()
    fill(254,255,0)
    translate(m,0)
    scale(b,1)
    rect(-60,400,100,50)
    fill(102,138,196)
    ellipse(10,380,30,50)
    strokeWeight(10)
    rect(-10,400,1,50)
    rect(10,400,1,50)
    point(-30,420)

    if mousePressed and (mouseButton == LEFT):
        line(mouseX,mouseY,pmouseX,pmouseY) 
    elif mousePressed and (mouseButton == RIGHT):
        
        strokeWeight(1000)
        stroke(255,250,250)
    elif mousePressed and (mouseButton == CENTER):
        strokeWeight(10)
        stroke(3,3,3)
    pop()
    push()
    fill(246,255,3)
    ellipse(900,100,50,50)
    pop()
    push()
    fill(3,255,80)
    rect(450,500,10,500)
    pop()
    translate(450,450)
    ellipse(0,0,30,30)
    fill(255,250,250)
    rotate(radians(30))
    ellipse(80,0,100,40)
    rotate(radians(30))
    ellipse(80,0,100,40)
    rotate(radians(30))
    ellipse(80,0,100,40)
    rotate(radians(30))
    ellipse(80,0,100,40)
    rotate(radians(30))
    ellipse(80,0,100,40)
    rotate(radians(30))
    ellipse(80,0,100,40)
    rotate(radians(30))
    ellipse(80,0,100,40)
    rotate(radians(30))
    ellipse(80,0,100,40)
    rotate(radians(30))
    ellipse(80,0,100,40)
    rotate(radians(30))
    ellipse(80,0,100,40)
    
    rotate(radians(30))
    ellipse(80,0,100,40)
    rotate(radians(30))
    ellipse(80,0,100,40)
    rotate(radians(30))
    ellipse(80,0,100,40)
    rotate(radians(30))
    ellipse(80,0,100,40)
    
    rotate(radians(30))
    ellipse(80,0,100,40)
    rotate(radians(30))
    ellipse(80,0,100,40)
    rotate(radians(30))
    ellipse(80,0,100,40)
    
    rotate(radians(30))
    ellipse(80,0,100,40)
    rotate(radians(30))
    ellipse(80,0,100,40)
    rotate(radians(30))
    ellipse(80,0,100,40)
    rotate(radians(30))
    ellipse(80,0,100,40)
    rotate(radians(30))
    ellipse(80,0,100,40)
    
    rotate(radians(30))
    ellipse(80,0,100,40)
    rotate(radians(30))
    ellipse(80,0,100,40)
    
    rotate(radians(30))
    ellipse(80,0,100,40)
    rotate(radians(30))
    ellipse(80,0,100,40)
    rotate(radians(30))
    ellipse(80,0,100,40)
    
    rotate(radians(30))
    ellipse(80,0,100,40)
    rotate(radians(30))
    ellipse(80,0,100,40)
    rotate(radians(30))
    ellipse(80,0,100,40)
    
    rotate(radians(30))
    ellipse(80,0,100,40)
    rotate(radians(30))
    ellipse(80,0,100,40)
        
def mouseClicked():
    global x,HAnpoBLeHue,HAnpoBLeHue2
    if mouseButton == RIGHT:
        loop()
   

    
def keyPressed():
    global x,n,m,b
    if key == CODED:
        if keyCode == RIGHT:
            n = -1   
            x = x + 10
            
        if keyCode == LEFT:
            n = 1   
            x = x - 10
            
        if keyCode == DOWN:
                b = -1   
                m = m + 10
    
            
        if keyCode == UP:
            b=1
            m = m - 10
