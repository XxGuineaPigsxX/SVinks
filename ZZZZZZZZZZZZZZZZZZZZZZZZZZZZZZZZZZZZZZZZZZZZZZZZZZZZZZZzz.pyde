x=0 
n=-1
fillVal = 0
HAnpoBLeHue="право"  
def setup():
    size(600,600)
    frameRate(120)

def draw():
    
    background(217,245,252)
    global x,HAnpoBLeHue,n
    fill(254,255,0)

    translate(x,0)
    scale(n,1)
    rect(-30,300,100,50)
    fill(132,138,196)
    ellipse(40,280,30,50)
    strokeWeight(5)
    rect(20,300,1,50)
    rect(40,300,1,50)
    point(0,320)

    if mousePressed and (mouseButton == LEFT):
        line(mouseX,mouseY,pmouseX,pmouseY) 
    elif mousePressed and (mouseButton == RIGHT):
        
        strokeWeight(150)
        stroke(227,163,237)
    elif mousePressed and (mouseButton == CENTER):
        strokeWeight(10)
        stroke(203,105,105)

def mouseClicked():
    global x,HAnpoBLeHue
    if mouseButton == RIGHT:
        loop()
   
if HAnpoBLeHue == "право":
    x = x + 10
    
if HAnpoBLeHue == "влево":

    x = x - 10
if x >= 600:
    HAnpoBLeHue = "влево"

    n=1
if x <= 0:
    
    HAnpoBLeHue = "право" 
    n = -1
    
def keyPressed():
    global x,n
    if key == CODED:
        if keyCode == RIGHT:
            n = -1   
            x = x + 10
    
            
    if keyCode == LEFT:
        n=1
        x = x - 10
