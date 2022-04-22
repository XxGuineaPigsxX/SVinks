def setup(): 
    size(600,400)
    background(100)
def draw():
    if mousePressed and (mouseButton == LEFT):
        line(mouseX,mouseY,pmouseX,pmouseY) 
    elif mousePressed and (mouseButton == RIGHT):
        
        strokeWeight(150)
        stroke(227,163,237)
    elif mousePressed and (mouseButton == CENTER):
        strokeWeight(10)
        stroke(203,105,105)

    

def mouseClicked():
    if mouseButton == RIGHT:
        loop()   
