x=0 
n=-1
HAnpoBLeHue="право"  
def setup():
    size(600,600)

def draw():
    background(250)
    global x,HAnpoBLeHue,n
    fill(254,255,0)
    

    translate(x,0)
    scale(n,1)
    rect(0,300,100,50)
    fill(132,138,196)
    ellipse(70,280,30,50)
    strokeWeight(5)
    rect(50,300,1,50)
    rect(70,300,1,50)
    point(30,320)
    

    
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
    
