x = 0;
ochki= 0;

def setup():
    size(600,400)
    
def draw():
    global x,ochki
    background(x)
    fill(43,142,55) 
    rect(250,150,100,50)
    fill(18,118,13)
    ellipse(300,175,50,50)
    fill(8,103,3)
    ellipse(300,175,20,40)
    textSize(30)
    textAlign(CENTER,CENTER)
    fill(255,0,0)
    
    text(ochki,200,300)
    text(u"$",250,300) 

def mouseClicked():
    global x,ochki
    
    if mouseX > 250 and mouseX < 350 and mouseY > 150 and mouseY < 200:
        x = 255
        ochki = ochki + 100
    
    

    
    
    
