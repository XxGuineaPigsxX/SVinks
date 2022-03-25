

def setup():
    size(900,900)
    background(0)
def draw():
 

    fill(134,23,23)
    ellipse(450,550,60,200)
    translate(450,450)
    ellipse(50,-25,50,50)
    ellipse(-45,-30,50,50)
    ellipse(0,0,100,100)
    ellipse(0,0,0,100)
    ellipse(0,0,100,0)
    
    push()
    translate(50,100)
    rotate(radians(330))
    ellipse(0,0,30,100)
    pop()
    push()
    translate(-50,100)
    rotate(radians(30))
    ellipse(0,0,30,100)
    pop()
    push()
    translate(-30,240)
    rotate(radians(30))
    ellipse(0,0,30,100)
    pop()
    push()
    translate(30,240)
    rotate(radians(330))
    ellipse(0,0,30,100)
    pop()
    stroke (random(0,255),random(0,255),random(0,255))
    strokeWeight (random(2,8))
    point(random (-600,600),random (-500,500))
    fill(254,255,219)
    triangle(10+90,10,100+90,20,40+90,90)
    triangle(10+150,10,100+100,20,40+150,90)
    triangle(10+170,10,100+150,20,40+200,90)
    ellipse(228,-16,200,200);
    strokeWeight(5)
    point(130,50)
